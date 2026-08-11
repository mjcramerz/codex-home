package Codex::Hook::Environment;

use strict;
use warnings;

use Exporter qw(import);
use File::Spec;
use JSON::PP ();

use Codex::Hook::Runner qw(run_command);

our @EXPORT_OK = qw(
  command_exists
  environment_report
  stringify_payload_text
);

my %COMMAND_CACHE;
my %PROBE_CACHE;

sub _trim {
    my ($value) = @_;
    return '' if !defined $value;
    $value =~ s/^\s+|\s+$//g;
    return $value;
}

sub _truncate {
    my ($text, $limit) = @_;
    $text = '' if !defined $text;
    return $text if !defined $limit;
    return $text if ref($limit) || $limit !~ /\A[0-9]+\z/ || $limit < 1;
    return $text if length($text) <= $limit;
    return substr($text, 0, $limit - 3) . '...';
}

sub _path_exts {
    return ('') if !$^O || $^O ne 'MSWin32';
    my $pathext = $ENV{PATHEXT} // '.COM;.EXE;.BAT;.CMD';
    my @exts = grep { length($_) } split /;/, $pathext;
    return ('', @exts);
}

sub command_exists {
    my ($command) = @_;
    return 0 if !defined $command || $command !~ /\A[A-Za-z0-9][A-Za-z0-9+_.-]*\z/;
    my $cache_key = join("\0", $command, ($ENV{PATH} // ''));
    return $COMMAND_CACHE{$cache_key} if exists $COMMAND_CACHE{$cache_key};

    for my $dir (File::Spec->path()) {
        next if !defined $dir || !length $dir;
        for my $ext (_path_exts()) {
            my $candidate = File::Spec->catfile($dir, $command . $ext);
            next if !-f $candidate;
            return $COMMAND_CACHE{$cache_key} = 1 if -x $candidate;
        }
    }
    return $COMMAND_CACHE{$cache_key} = 0;
}

sub stringify_payload_text {
    my (%args) = @_;
    my $value = $args{value};
    return '' if !defined $value;
    return _truncate($value, $args{limit}) if !ref($value);
    if (ref($value) eq 'ARRAY') {
        my @parts = grep { defined($_) && !ref($_) && length _trim($_) } @{$value};
        return _truncate(join(' ', @parts), $args{limit}) if @parts;
    }

    if (ref($value) eq 'HASH') {
        my @parts;
        for my $key (qw(cmd command stdout stderr text reason stopReason message)) {
            my $item = $value->{$key};
            next if !defined $item;
            if (ref($item) eq 'ARRAY') {
                my @values = grep { defined($_) && !ref($_) && length _trim($_) } @{$item};
                push @parts, "$key: " . join(' ', @values) if @values;
                next;
            }
            next if ref($item) || !length _trim($item);
            push @parts, "$key: " . _trim($item);
        }
        if (@parts) {
            return _truncate(join("\n", @parts), $args{limit});
        }
    }

    my $json = eval { JSON::PP->new->canonical(1)->allow_nonref(1)->encode($value) };
    return '' if !$json || $@;
    return _truncate($json, $args{limit});
}

sub _append_unique {
    my ($target, $seen, @values) = @_;
    for my $value (@values) {
        next if !defined $value || !length $value;
        next if $seen->{$value}++;
        push @{$target}, $value;
    }
}

sub _probe_output_detail {
    my ($result) = @_;
    for my $source ($result->{stderr}, $result->{stdout}) {
        next if !defined $source || !length $source;
        for my $line (split /\n/, $source) {
            my $trimmed = _trim($line);
            next if !length $trimmed;
            return _truncate($trimmed);
        }
    }
    return '';
}

sub _probe_result {
    my (%args) = @_;
    my $label = $args{label} // 'probe';
    my $command = $args{command};
    my $cwd = $args{cwd};
    my $timeout = $args{timeout} // 5;

    my $command_name = ref($command) eq 'ARRAY' && @{$command} ? ($command->[0] // '') : '';
    my $cache_key = join("\0", $label, ($cwd // ''), map { defined($_) ? $_ : '' } @{ $command || [] });
    return $PROBE_CACHE{$cache_key} if exists $PROBE_CACHE{$cache_key};

    if (!length($command_name) || !command_exists($command_name)) {
        return $PROBE_CACHE{$cache_key} = {
            label  => $label,
            status => 'missing-command',
            detail => length($command_name) ? "missing `$command_name`" : 'missing probe command',
        };
    }

    my $result = run_command(
        command => $command,
        cwd     => $cwd,
        timeout => $timeout,
    );
    if ($result->{rc} == 0) {
        my $detail = _probe_output_detail($result);
        return $PROBE_CACHE{$cache_key} = {
            label  => $label,
            status => 'ok',
            detail => $detail,
        };
    }
    if ($result->{rc} == 124) {
        return $PROBE_CACHE{$cache_key} = {
            label  => $label,
            status => 'timeout',
            detail => 'timed out',
        };
    }
    my $detail = _probe_output_detail($result);
    return $PROBE_CACHE{$cache_key} = {
        label  => $label,
        status => 'failed',
        detail => length($detail) ? $detail : "exit code $result->{rc}",
    };
}

sub environment_report {
    my (%args) = @_;
    my $blocks = $args{blocks};
    return {
        required_available => [],
        required_missing   => [],
        optional_available => [],
        optional_missing   => [],
        probes             => [],
    } if ref($blocks) ne 'ARRAY' || !@{$blocks};

    my (@required, @optional, @probes);
    my (%required_seen, %optional_seen, %probe_seen);
    for my $block (@{$blocks}) {
        next if ref($block) ne 'HASH';
        _append_unique(\@required, \%required_seen, @{ $block->{required_commands} || [] });
        _append_unique(\@optional, \%optional_seen, @{ $block->{optional_commands} || [] });
        for my $probe (@{ $block->{optional_probes} || [] }) {
            next if ref($probe) ne 'HASH';
            my $label = _trim($probe->{label});
            next if !length $label || $probe_seen{$label}++;
            push @probes, $probe;
        }
    }

    my (@required_available, @required_missing, @optional_available, @optional_missing);
    for my $command (@required) {
        if (command_exists($command)) {
            push @required_available, $command;
        } else {
            push @required_missing, $command;
        }
    }
    for my $command (@optional) {
        if (command_exists($command)) {
            push @optional_available, $command;
        } else {
            push @optional_missing, $command;
        }
    }

    my @probe_results = map {
        _probe_result(
            label   => $_->{label},
            command => $_->{command},
            cwd     => $args{cwd},
            timeout => $args{probe_timeout} // 5,
        )
    } @probes;

    return {
        required_available => \@required_available,
        required_missing   => \@required_missing,
        optional_available => \@optional_available,
        optional_missing   => \@optional_missing,
        probes             => \@probe_results,
    };
}

1;
