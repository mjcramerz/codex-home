package Codex::Hook::Subagent;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(start_context);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

# Avoid a second role-instruction stream beside runner.py.
sub start_context { return undef; }

1;
