package Codex::Hook::Driver;

use strict;
use warnings;
use Exporter qw(import);
use File::Basename qw(dirname);
use File::Spec;
use Cwd qw(abs_path);

our @EXPORT_OK = qw(run_event);

sub run_event {
    my ($event) = @_;
    die "Pass one event name.\n" if !defined($event) || ref($event);
    my $root = abs_path(File::Spec->catdir(dirname(__FILE__), '..', '..', '..'));
    die "Cannot resolve the reviewed hook installation.\n" if !defined($root);
    my $runner = File::Spec->catfile($root, 'runner.py');
    exec { '/usr/bin/python3' } '/usr/bin/python3', '-I', $runner,
        '--event', $event, '--timeout', '3';
    die "Cannot start the repository-context hook.\n";
}

1;
