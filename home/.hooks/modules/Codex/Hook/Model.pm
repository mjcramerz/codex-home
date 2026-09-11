package Codex::Hook::Model;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(canonical_event_name event_script_name normalize_input known_event_args);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

my %EVENTS = (
    'session-start' => ['SessionStart', 'session_start.pl'],
    'session-end' => ['SessionEnd', 'session_end.pl'],
    'user-prompt-submit' => ['UserPromptSubmit', 'user_prompt_submit.pl'],
    'pre-tool-use' => ['PreToolUse', 'pre_tool_use.pl'],
    'permission-request' => ['PermissionRequest', 'permission_request.pl'],
    'post-tool-use' => ['PostToolUse', 'post_tool_use.pl'],
    'pre-compact' => ['PreCompact', 'pre_compact.pl'],
    'post-compact' => ['PostCompact', 'post_compact.pl'],
    'subagent-start' => ['SubagentStart', 'subagent_start.pl'],
    'subagent-stop' => ['SubagentStop', 'subagent_stop.pl'],
    'stop' => ['Stop', 'stop.pl'],
    'interrupt' => ['Interrupt', 'interrupt.pl'],
);
sub known_event_args { return sort keys %EVENTS; }
sub _event_meta {
    my ($name) = @_;
    die "Pass a supported hook event.\n" if !defined($name) || ref($name);
    return $EVENTS{$name} if exists $EVENTS{$name};
    for my $meta (values %EVENTS) { return $meta if $meta->[0] eq $name; }
    die "Pass a supported hook event.\n";
}
sub canonical_event_name { return _event_meta($_[0])->[0]; }
sub event_script_name { return _event_meta($_[0])->[1]; }
sub normalize_input {
    my ($event, $payload) = @_;
    die "Pass an object payload.\n" if ref($payload) ne 'HASH';
    my $canonical = canonical_event_name($event);
    die "Do not change the payload event.\n"
        if exists($payload->{hook_event_name}) && $payload->{hook_event_name} ne $canonical;
    return { %{$payload}, hook_event_name => $canonical };
}

1;
