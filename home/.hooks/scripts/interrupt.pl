#!/usr/bin/env perl
# Clear digest-only session context after an interruption.
use strict;
use warnings;
use FindBin qw($RealBin);
exec { '/usr/bin/python3' } '/usr/bin/python3', '-I', "$RealBin/../runner.py", '--event', 'Interrupt';
die "Cannot dispatch Interrupt.\n";
