package Codex::Hook::Schema;

use strict;
use warnings;

use Cwd qw(getcwd);
use Exporter qw(import);
use File::Spec;
use JSON::PP qw(decode_json);
use Scalar::Util qw(blessed);

use Codex::Hook::Model qw(canonical_event_name);

our @EXPORT_OK = qw(
  validate_event_input
  validate_event_output
);

my %SCHEMA_CACHE;
my %SCHEMA_DIR_CACHE;

sub _event_basename {
    my ($event_arg) = @_;
    return $event_arg . '.command';
}

sub _candidate_schema_dirs {
    my (%args) = @_;
    my @bases;
    for my $raw ($args{repo_root}, $args{cwd}, getcwd()) {
        next if !defined $raw || !length $raw;
        push @bases, $raw;
    }

    my @relative_candidates = (
        [qw(codex-rs hooks schema generated)],
        [qw(hooks schema generated)],
        ['..', 'codex', 'codex-rs', 'hooks', 'schema', 'generated'],
        ['..', '..', 'codex', 'codex-rs', 'hooks', 'schema', 'generated'],
    );

    my @dirs;
    if (defined $ENV{CODEX_HOOK_SCHEMA_DIR} && length $ENV{CODEX_HOOK_SCHEMA_DIR}) {
        push @dirs, $ENV{CODEX_HOOK_SCHEMA_DIR};
    }
    for my $base (@bases) {
        for my $parts (@relative_candidates) {
            push @dirs, File::Spec->catdir($base, @{$parts});
        }
    }

    my @unique;
    my %seen;
    for my $dir (@dirs) {
        next if $seen{$dir}++;
        push @unique, $dir;
    }
    return @unique;
}

sub _schema_dir {
    my (%args) = @_;
    my $cache_key = join("\0", map { defined($_) ? $_ : '' } ($args{repo_root}, $args{cwd}));
    return $SCHEMA_DIR_CACHE{$cache_key} if exists $SCHEMA_DIR_CACHE{$cache_key};

    for my $dir (_candidate_schema_dirs(%args)) {
        if (-d $dir) {
            return $SCHEMA_DIR_CACHE{$cache_key} = $dir;
        }
    }
    return $SCHEMA_DIR_CACHE{$cache_key} = undef;
}

sub _schema_path {
    my ($event_arg, $direction, %args) = @_;
    my $root = _schema_dir(%args);
    return undef if !defined $root || !length $root;
    my $path = File::Spec->catfile($root, _event_basename($event_arg) . '.' . $direction . '.schema.json');
    return -f $path ? $path : undef;
}

sub _load_schema {
    my ($event_arg, $direction, %args) = @_;
    my $cache_key = join("\0", $event_arg, $direction, map { defined($_) ? $_ : '' } ($args{repo_root}, $args{cwd}));
    return $SCHEMA_CACHE{$cache_key} if exists $SCHEMA_CACHE{$cache_key};

    my $path = _schema_path($event_arg, $direction, %args);
    return $SCHEMA_CACHE{$cache_key} = undef if !defined $path;

    open my $fh, '<:encoding(UTF-8)', $path or die "unable to read hook schema $path: $!\n";
    local $/;
    my $raw = <$fh>;
    close $fh;
    my $schema = decode_json($raw);
    die "hook schema must decode to an object: $path\n" if ref($schema) ne 'HASH';
    return $SCHEMA_CACHE{$cache_key} = $schema;
}

sub _resolve_ref {
    my ($schema, $ref) = @_;
    die "unsupported schema ref: $ref\n" if !defined $ref || $ref !~ m{\A#/};
    my $node = $schema;
    for my $part (split m{/}, substr($ref, 2)) {
        $part =~ s/~1/\//g;
        $part =~ s/~0/~/g;
        die "schema ref target missing for $ref\n" if ref($node) ne 'HASH' || !exists $node->{$part};
        $node = $node->{$part};
    }
    die "schema ref target must be an object for $ref\n" if ref($node) ne 'HASH';
    return $node;
}

sub _effective_schema {
    my ($schema, $node) = @_;
    return {} if ref($node) ne 'HASH';
    my %merged = %{ $node // {} };
    if (exists $merged{'$ref'}) {
        my $target = _resolve_ref($schema, delete $merged{'$ref'});
        my %resolved = %{ _effective_schema($schema, $target) };
        @resolved{keys %merged} = values %merged;
        %merged = %resolved;
    }
    if (ref($merged{allOf}) eq 'ARRAY') {
        my @parts = @{ delete $merged{allOf} };
        my %combined = ();
        for my $part (@parts) {
            next if ref($part) ne 'HASH';
            my %resolved = %{ _effective_schema($schema, $part) };
            @combined{keys %resolved} = values %resolved;
        }
        @combined{keys %merged} = values %merged;
        %merged = %combined;
    }
    return \%merged;
}

sub _is_boolean {
    my ($value) = @_;
    return 1 if blessed($value) && blessed($value) =~ /Boolean/;
    return !ref($value) && ($value eq '0' || $value eq '1');
}

sub _matches_type {
    my ($value, $schema_type) = @_;
    return 1 if !defined $schema_type;
    if (ref($schema_type) eq 'ARRAY') {
        for my $candidate (@{$schema_type}) {
            return 1 if _matches_type($value, $candidate);
        }
        return 0;
    }
    return !defined($value) if $schema_type eq 'null';
    return !ref($value) if $schema_type eq 'string';
    return _is_boolean($value) if $schema_type eq 'boolean';
    return ref($value) eq 'HASH' if $schema_type eq 'object';
    return ref($value) eq 'ARRAY' if $schema_type eq 'array';
    return !ref($value) && $value =~ /\A-?(?:0|[1-9][0-9]*)\z/ if $schema_type eq 'integer';
    return !ref($value) && $value =~ /\A-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?\z/ if $schema_type eq 'number';
    return 1;
}

sub _validate_node {
    my ($schema, $node, $value, $label) = @_;
    return if ref($node) ne 'HASH';
    my $effective = _effective_schema($schema, $node);

    if (exists $effective->{const}) {
        my $expected = $effective->{const};
        die "$label must equal $expected\n" if (!defined $value && defined $expected) || (defined $value && (!defined $expected || $value ne $expected));
    }
    if (ref($effective->{enum}) eq 'ARRAY') {
        my %allowed = map { defined($_) ? ($_ => 1) : () } @{ $effective->{enum} };
        die "$label must be one of the allowed enum values\n" if defined $value && !$allowed{$value};
    }
    if (exists $effective->{type} && !_matches_type($value, $effective->{type})) {
        die "$label does not match schema type\n";
    }

    return if ref($value) ne 'HASH' || ref($effective->{properties}) ne 'HASH';

    if ($effective->{additionalProperties} && ref($effective->{additionalProperties}) ne 'HASH') {
        # additionalProperties=true is effectively unbounded; false is handled below.
    }
    if (exists $effective->{additionalProperties} && !$effective->{additionalProperties}) {
        for my $key (keys %{$value}) {
            die "$label contains unsupported key $key\n" if !exists $effective->{properties}{$key};
        }
    }

    if (ref($effective->{required}) eq 'ARRAY') {
        for my $key (@{ $effective->{required} }) {
            die "$label is missing required key $key\n" if !exists $value->{$key};
        }
    }

    for my $key (keys %{ $effective->{properties} }) {
        next if !exists $value->{$key};
        _validate_node($schema, $effective->{properties}{$key}, $value->{$key}, "$label.$key");
    }
}

sub validate_event_input {
    my ($event_arg, $payload, %args) = @_;
    my $schema = _load_schema($event_arg, 'input', %args);
    return if !defined $schema;
    _validate_node($schema, $schema, $payload, canonical_event_name($event_arg) . '.input');
}

sub validate_event_output {
    my ($event_arg, $payload, %args) = @_;
    my $schema = _load_schema($event_arg, 'output', %args);
    return if !defined $schema;
    _validate_node($schema, $schema, $payload, canonical_event_name($event_arg) . '.output');
}

1;
