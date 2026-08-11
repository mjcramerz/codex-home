package Codex::Hook::Repo;

use strict;
use warnings;

use Exporter qw(import);
use File::Spec;

use Codex::Hook::Runner qw(run_command);

our @EXPORT_OK = qw(
  git_root
  current_branch
  has_salsa_packaging_layout
  list_mirror_refs
  list_packaging_refs
  preferred_mirror_main_branch
  list_changed_files
  summarize_worktree
  preview_paths
  has_patch_release_dir
);

my %ROOT_CACHE;
my %REF_CACHE;
my %STATUS_CACHE;

sub git_root {
    my ($cwd) = @_;
    return undef if !defined $cwd || !length $cwd;
    return $ROOT_CACHE{$cwd} if exists $ROOT_CACHE{$cwd};
    my $result = run_command(
        command => ['git', '-C', $cwd, 'rev-parse', '--show-toplevel'],
        timeout => 8,
    );
    return $ROOT_CACHE{$cwd} = undef if $result->{rc} != 0;
    my $root = $result->{stdout} // '';
    $root =~ s/^\s+|\s+$//g;
    return $ROOT_CACHE{$cwd} = (length($root) ? $root : undef);
}

sub _parse_branch_line {
    my ($line) = @_;
    return '' if !defined $line || $line !~ /\A##\s+/;
    my $content = substr($line, 3);
    return 'detached' if $content =~ /\AHEAD\b/;
    my ($branch) = split /\.\.\./, $content, 2;
    $branch =~ s/\s+\z//;
    return $branch;
}

sub _status_snapshot {
    my ($repo_root) = @_;
    return $STATUS_CACHE{$repo_root} if exists $STATUS_CACHE{$repo_root};

    my $result = run_command(
        command => ['git', '-C', $repo_root, 'status', '--branch', '--porcelain=v1', '--untracked-files=all', '--no-renames'],
        timeout => 12,
    );
    my %snapshot = (
        branch       => 'detached',
        changed_files => [],
        preview      => [],
        counts       => {
            staged    => 0,
            unstaged  => 0,
            untracked => 0,
            deleted   => 0,
            renamed   => 0,
            conflicts => 0,
            preview   => [],
        },
    );
    return $STATUS_CACHE{$repo_root} = \%snapshot if $result->{rc} != 0;

    my @lines = split /\n/, ($result->{stdout} // '');
    if (@lines && $lines[0] =~ /\A##\s+/) {
        $snapshot{branch} = _parse_branch_line($lines[0]);
        shift @lines;
    }

    my @preview;
    for my $raw_line (@lines) {
        next if length($raw_line) < 4;
        my $x = substr($raw_line, 0, 1);
        my $y = substr($raw_line, 1, 1);
        my $path = _parse_status_path($raw_line);
        next if !length $path;

        push @{ $snapshot{changed_files} }, $path;
        if (!grep { $_ eq $path } @preview) {
            push @preview, $path;
        }
        if ($x eq '?' && $y eq '?') {
            $snapshot{counts}{untracked}++;
            next;
        }
        $snapshot{counts}{staged}++ if $x ne ' ' && $x ne '?';
        $snapshot{counts}{unstaged}++ if $y ne ' ' && $y ne '?';
        $snapshot{counts}{deleted}++ if $x eq 'D' || $y eq 'D';
        $snapshot{counts}{renamed}++ if $x eq 'R' || $y eq 'R';
        $snapshot{counts}{conflicts}++ if $x eq 'U' || $y eq 'U' || ($x eq 'A' && $y eq 'A') || ($x eq 'D' && $y eq 'D');
    }
    $snapshot{counts}{preview} = [ @preview ] if @preview;
    return $STATUS_CACHE{$repo_root} = \%snapshot;
}

sub current_branch {
    my ($repo_root) = @_;
    my $snapshot = _status_snapshot($repo_root);
    my $branch = $snapshot->{branch} // '';
    return $branch if length($branch) && $branch ne 'detached';

    my $detached = run_command(
        command => ['git', '-C', $repo_root, 'rev-parse', '--short', 'HEAD'],
        timeout => 8,
    );
    my $sha = $detached->{stdout} // '';
    $sha =~ s/^\s+|\s+$//g;
    return length($sha) ? $sha : 'detached';
}

sub _list_refs {
    my ($repo_root) = @_;
    return @{ $REF_CACHE{$repo_root} } if exists $REF_CACHE{$repo_root};
    my $result = run_command(
        command => [
            'git',
            '-C',
            $repo_root,
            'for-each-ref',
            '--format=%(refname:short)',
            'refs/heads',
            'refs/remotes',
            'refs/tags',
        ],
        timeout => 10,
    );
    return @{ $REF_CACHE{$repo_root} = [] } if $result->{rc} != 0;
    my @refs = grep { length $_ } map { s/^\s+|\s+$//gr } split /\n/, ($result->{stdout} // '');
    $REF_CACHE{$repo_root} = \@refs;
    return @refs;
}

sub list_mirror_refs {
    my ($repo_root) = @_;
    return grep { $_ =~ m{\A(?:github|gitlab|origin/github|origin/gitlab)/} } _list_refs($repo_root);
}

sub list_packaging_refs {
    my ($repo_root) = @_;
    return grep {
        $_ eq 'pristine-tar'
          || $_ eq 'origin/pristine-tar'
          || $_ =~ m{\A(?:origin/)?upstream/}
          || $_ =~ m{\A(?:origin/)?debian/}
    } _list_refs($repo_root);
}

sub has_salsa_packaging_layout {
    my ($repo_root) = @_;
    my @mirror_refs = list_mirror_refs($repo_root);
    return 0 if !grep { $_ =~ m{\A(?:gitlab|origin/gitlab)/} } @mirror_refs;

    my @packaging_refs = list_packaging_refs($repo_root);
    my $has_pristine = grep { $_ eq 'pristine-tar' || $_ eq 'origin/pristine-tar' } @packaging_refs;
    return $has_pristine ? 1 : 0;
}

sub preferred_mirror_main_branch {
    my ($repo_root) = @_;
    my %refs = map { $_ => 1 } list_mirror_refs($repo_root);
    for my $candidate (
        'github/mcr/main',
        'gitlab/mcr/main',
    ) {
        return $candidate if $refs{$candidate};
    }
    return '';
}

sub _git_status_lines {
    my ($repo_root) = @_;
    my $snapshot = _status_snapshot($repo_root);
    return @{ $snapshot->{changed_files} };
}

sub _parse_status_path {
    my ($raw_line) = @_;
    return '' if !defined $raw_line || length($raw_line) < 4;
    my $path = substr($raw_line, 3);
    if ($path =~ / -> /) {
        ($path) = $path =~ / -> (.+)\z/;
    }
    $path =~ s/^\s+|\s+$//g;
    return $path;
}

sub list_changed_files {
    my ($repo_root) = @_;
    my $snapshot = _status_snapshot($repo_root);
    return @{ $snapshot->{changed_files} };
}

sub summarize_worktree {
    my ($repo_root) = @_;
    my $snapshot = _status_snapshot($repo_root);
    my %counts = %{ $snapshot->{counts} };
    return \%counts;
}

sub preview_paths {
    my ($paths, $limit) = @_;
    return 'none' if ref($paths) ne 'ARRAY' || !@{$paths};
    my @unique;
    my %seen;
    for my $path (@{$paths}) {
        next if !$path || $seen{$path}++;
        push @unique, $path;
    }
    if (defined $limit && $limit =~ /\A[0-9]+\z/ && $limit > 0 && @unique > $limit) {
        my $last = $limit - 1;
        my $rendered = join(', ', @unique[0 .. $last]);
        my $remaining = @unique - ($last + 1);
        $rendered .= " (+$remaining more)" if $remaining > 0;
        return $rendered;
    }
    return join(', ', @unique);
}

sub has_patch_release_dir {
    my ($repo_root) = @_;
    return -d File::Spec->catdir($repo_root, 'patches', 'release');
}

1;
