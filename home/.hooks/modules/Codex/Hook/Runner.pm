package Codex::Hook::Runner;

use strict;
use warnings;

use Cwd qw(getcwd);
use Exporter qw(import);
use Fcntl qw(F_GETFL F_SETFL O_NONBLOCK);
use IO::Select;
use IPC::Open3 qw(open3);
use POSIX qw(:sys_wait_h);
use Symbol qw(gensym);

our @EXPORT_OK = qw(
  run_command
  read_file_tail
);

sub _validate_timeout {
    my ($timeout) = @_;
    $timeout = 10 if !defined $timeout;
    die "timeout must be a positive integer" if ref($timeout) || $timeout !~ /\A[0-9]+\z/ || $timeout < 1 || $timeout > 600;
    return int($timeout);
}

sub _validate_command {
    my ($command) = @_;
    die "command must be an array reference" if ref($command) ne 'ARRAY' || !@{$command};
    for my $part (@{$command}) {
        die "command entries must be defined scalars" if !defined $part || ref($part);
        die "command entries must not contain NUL bytes" if $part =~ /\x00/;
    }
    return $command;
}

sub _set_nonblocking {
    my ($handle) = @_;
    my $flags = fcntl($handle, F_GETFL, 0);
    return if !defined $flags;
    fcntl($handle, F_SETFL, $flags | O_NONBLOCK);
}

sub _drain_handles {
    my (%args) = @_;
    my $selector = $args{selector};
    my $stdout_ref = $args{stdout_ref};
    my $stderr_ref = $args{stderr_ref};
    my $deadline = $args{deadline};
    my %targets = %{ $args{targets} };

    while ($selector->count()) {
        my $remaining = $deadline - time();
        return 0 if $remaining <= 0;
        my @ready = $selector->can_read($remaining > 1 ? 1 : $remaining);
        next if !@ready;
        for my $handle (@ready) {
            my $buffer = '';
            my $read = sysread($handle, $buffer, 8192);
            if (!defined $read) {
                next if $!{EAGAIN} || $!{EWOULDBLOCK};
                $selector->remove($handle);
                close $handle;
                next;
            }
            if ($read == 0) {
                $selector->remove($handle);
                close $handle;
                next;
            }
            if ($targets{$handle} eq 'stdout') {
                ${$stdout_ref} .= $buffer;
            } else {
                ${$stderr_ref} .= $buffer;
            }
        }
    }
    return 1;
}

sub run_command {
    my (%args) = @_;
    my $command = _validate_command($args{command});
    my $cwd = $args{cwd};
    my $timeout = _validate_timeout($args{timeout});

    my $previous_cwd = getcwd();
    my $changed_cwd = 0;
    if (defined $cwd && length $cwd) {
        chdir $cwd or return { rc => 1, stdout => '', stderr => "unable to chdir to $cwd: $!" };
        $changed_cwd = 1;
    }

    my ($stdout, $stderr) = ('', '');
    my $stdout_handle;
    my $stderr_handle = gensym();
    my $pid;
    my $spawn_ok = eval {
        $pid = open3(undef, $stdout_handle, $stderr_handle, @{$command});
        1;
    };
    my $spawn_error = $@;
    if ($changed_cwd) {
        chdir $previous_cwd or die "failed to restore working directory to $previous_cwd: $!";
    }
    return { rc => 1, stdout => '', stderr => $spawn_error || 'command failed to start' } if !$spawn_ok;

    _set_nonblocking($stdout_handle) if defined $stdout_handle;
    _set_nonblocking($stderr_handle);

    my $selector = IO::Select->new();
    my %targets;
    if (defined $stdout_handle) {
        $selector->add($stdout_handle);
        $targets{$stdout_handle} = 'stdout';
    }
    if (defined $stderr_handle) {
        $selector->add($stderr_handle);
        $targets{$stderr_handle} = 'stderr';
    }

    my $deadline = time() + $timeout;
    my $timed_out = 0;
    my $pid_exited = 0;
    my $wait_status = 0;
    while (1) {
        if (!$pid_exited) {
            my $wait = waitpid($pid, WNOHANG);
            if ($wait == $pid) {
                $pid_exited = 1;
                $wait_status = $?;
            }
        }
        last if $pid_exited && !$selector->count();
        if (!_drain_handles(
                selector   => $selector,
                stdout_ref => \$stdout,
                stderr_ref => \$stderr,
                deadline   => $deadline,
                targets    => \%targets,
            )) {
            $timed_out = 1;
            last;
        }
        if (!$pid_exited) {
            my $wait = waitpid($pid, WNOHANG);
            if ($wait == $pid) {
                $pid_exited = 1;
                $wait_status = $?;
            }
        }
        last if $pid_exited && !$selector->count();
    }

    if ($timed_out) {
        kill 'TERM', $pid;
        my $grace_deadline = time() + 2;
        _drain_handles(
            selector   => $selector,
            stdout_ref => \$stdout,
            stderr_ref => \$stderr,
            deadline   => $grace_deadline,
            targets    => \%targets,
        );
        if (waitpid($pid, WNOHANG) == 0) {
            kill 'KILL', $pid;
            waitpid($pid, 0);
        }
        return { rc => 124, stdout => $stdout, stderr => 'command timed out' };
    }

    if (!$pid_exited) {
        my $waited = waitpid($pid, 0);
        if ($waited == $pid) {
            $pid_exited = 1;
            $wait_status = $?;
        }
    }
    my $rc = $pid_exited ? ($wait_status >> 8) : 1;
    return {
        rc     => $rc,
        stdout => $stdout // '',
        stderr => $stderr // '',
    };
}

sub read_file_tail {
    my (%args) = @_;
    my $path = $args{path};
    return '' if !defined $path || !length $path;
    return '' if !-f $path;
    my $has_limit = exists $args{max_bytes};
    my $max_bytes = $args{max_bytes};
    return '' if $has_limit && (ref($max_bytes) || $max_bytes !~ /\A[0-9]+\z/ || $max_bytes < 1);

    open my $fh, '<:raw', $path or return '';
    my $size = -s $fh;
    if ($has_limit && defined $size && $size > $max_bytes) {
        seek $fh, $size - $max_bytes, 0 or return '';
    }
    local $/;
    my $data = <$fh>;
    close $fh;
    return '' if !defined $data;
    return $data;
}

1;
