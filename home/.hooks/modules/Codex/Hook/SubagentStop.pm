package Codex::Hook::SubagentStop;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(stop_system_message);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

# Do not force a finish, re-run a task or invent validation at stop time.
sub stop_system_message { return undef; }

1;
