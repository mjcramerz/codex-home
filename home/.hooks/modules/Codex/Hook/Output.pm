package Codex::Hook::Output;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(json_true json_false emit_payload emit_context emit_system_message emit_stop emit_block);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

use JSON::PP qw(encode_json);
use Codex::Hook::Model qw(canonical_event_name);
our $CURRENT_EVENT_ARG;
sub json_true { return JSON::PP::true(); }
sub json_false { return JSON::PP::false(); }
sub _event {
    die "Set CURRENT_EVENT_ARG before emitting an event-specific result.\n" if !defined $CURRENT_EVENT_ARG;
    return canonical_event_name($CURRENT_EVENT_ARG);
}
sub emit_payload {
    my ($payload) = @_;
    die "Emit one JSON object.\n" if ref($payload) ne 'HASH';
    my $encoded = encode_json($payload);
    die "Keep hook output bounded.\n" if length($encoded) > 49152;
    print $encoded, "\n" or die "Cannot emit hook result.\n";
}
sub emit_context {
    my ($event, $context, $message) = @_;
    $event = canonical_event_name($event);
    my %payload;
    if ($event =~ /\A(?:SessionStart|UserPromptSubmit|SubagentStart|PreToolUse|PostToolUse)\z/ && defined($context) && !ref($context) && length($context)) {
        $payload{hookSpecificOutput} = { hookEventName => $event, additionalContext => substr($context, 0, 7200) };
    }
    $payload{systemMessage} = substr($message, 0, 512) if defined($message) && !ref($message) && length($message);
    emit_payload(\%payload);
}
sub emit_system_message {
    my ($message) = @_;
    die "Pass a bounded message.\n" if !defined($message) || ref($message);
    emit_payload({ systemMessage => substr($message, 0, 512) });
}
sub emit_block {
    my ($reason) = @_;
    die "Pass a nonempty reason.\n" if !defined($reason) || ref($reason) || $reason !~ /\S/;
    my $event = _event();
    $reason = substr($reason, 0, 512);
    if ($event eq 'PreToolUse') {
        emit_payload({ hookSpecificOutput => { hookEventName => $event, permissionDecision => 'deny', permissionDecisionReason => $reason } });
    } elsif ($event eq 'PermissionRequest') {
        emit_payload({ hookSpecificOutput => { hookEventName => $event, decision => { behavior => 'deny', message => $reason } } });
    } elsif ($event =~ /\A(?:UserPromptSubmit|Stop|SubagentStop)\z/) {
        emit_payload({ decision => 'block', reason => $reason });
    } else { die "Do not block this event through an unsupported result shape.\n"; }
}
sub emit_stop {
    my ($reason) = @_;
    my $event = _event();
    return emit_block($reason) if $event eq 'PreToolUse' || $event eq 'PermissionRequest';
    die "Pass a nonempty reason.\n" if !defined($reason) || ref($reason) || $reason !~ /\S/;
    emit_payload({ continue => JSON::PP::false(), stopReason => substr($reason, 0, 512) });
}

1;
