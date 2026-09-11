#!/usr/bin/env perl
# Dispatch this compatibility entrypoint without a shell or repository imports.
use strict;
use warnings;
use FindBin qw($RealBin);
use File::Spec;
my $event = "SessionStart";
die "Do not pass arguments to this named hook.\n" if @ARGV;
my $runner = File::Spec->catfile($RealBin, '..', 'runner.py');
exec { '/usr/bin/python3' } '/usr/bin/python3', '-I', $runner,
    '--event', $event, '--timeout', '3';
die "Cannot start the reviewed repository-context hook.\n";
