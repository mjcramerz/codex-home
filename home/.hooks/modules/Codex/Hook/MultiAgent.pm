package Codex::Hook::MultiAgent;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(multi_agent_prompt_context subagent_role_context);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

# Receive role-specific instructions once through the active SubagentStart hook.
sub multi_agent_prompt_context { return (); }
sub subagent_role_context { return (); }

1;
