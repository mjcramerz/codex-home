package Codex::Hook::Output;

use strict;
use warnings;

use Exporter qw(import);
use JSON::PP qw(encode_json);
use Codex::Hook::Schema qw(validate_event_output);

our @EXPORT_OK = qw(
  json_true
  json_false
  emit_payload
  emit_context
  emit_system_message
  emit_stop
  emit_block
);

our $CURRENT_EVENT_ARG;

sub json_true {
    return JSON::PP::true();
}

sub json_false {
    return JSON::PP::false();
}

sub emit_payload {
    my ($payload) = @_;
    validate_event_output($CURRENT_EVENT_ARG, $payload)
      if defined $CURRENT_EVENT_ARG && length $CURRENT_EVENT_ARG;
    print encode_json($payload), "\n";
}

sub emit_context {
    my ($event_name, $context, $system_message) = @_;
    my %payload = ( continue => JSON::PP::true() );
    if (defined $system_message && length $system_message) {
        $payload{systemMessage} = $system_message;
    }
    if (defined $context && length $context) {
        $payload{hookSpecificOutput} = {
            hookEventName    => $event_name,
            additionalContext => $context,
        };
    }
    return if keys(%payload) <= 1;
    emit_payload(\%payload);
}

sub emit_system_message {
    my ($system_message) = @_;
    return if !defined $system_message || !length $system_message;
    emit_payload({
        continue      => JSON::PP::true(),
        systemMessage => $system_message,
    });
}

sub emit_stop {
    my ($reason, $system_message) = @_;
    die "stop reason must not be empty\n" if !defined $reason || $reason !~ /\S/;
    my %payload = (
        continue   => JSON::PP::false(),
        stopReason => $reason,
    );
    if (defined $system_message && length $system_message) {
        $payload{systemMessage} = $system_message;
    }
    emit_payload(\%payload);
}

sub emit_block {
    my ($reason, $system_message) = @_;
    die "block reason must not be empty\n" if !defined $reason || $reason !~ /\S/;
    my %payload = (
        continue => JSON::PP::true(),
        decision => 'block',
        reason   => $reason,
    );
    if (defined $system_message && length $system_message) {
        $payload{systemMessage} = $system_message;
    }
    emit_payload(\%payload);
}

1;
