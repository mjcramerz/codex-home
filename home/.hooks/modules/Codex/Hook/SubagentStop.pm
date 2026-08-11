package Codex::Hook::SubagentStop;

use strict;
use warnings;

use Exporter qw(import);

use Codex::Hook::Environment qw(stringify_payload_text);
use Codex::Hook::Learning qw(transcript_summary_lines);

our @EXPORT_OK = qw(stop_system_message);

sub _trim {
    my ($value) = @_;
    return '' if !defined $value || ref($value);
    $value =~ s/^\s+|\s+$//g;
    return $value;
}

sub _handoff_signal_lines {
    my ($message) = @_;
    my $text = stringify_payload_text(value => $message);
    if (!length _trim($text)) {
        return (
            '- Last assistant message is empty; require an explicit subagent handoff before treating the work as complete.',
        );
    }

    my @lines;
    if ($text =~ /\b(?:could not run|couldn't run|unable to run|did not run|didn't run|skipped|cannot run|can't run|not run|permission denied|blocked)\b/i) {
        push @lines, '- Last assistant message reports skipped or blocked validation; parent-side validation or a concrete risk note is still required.';
    }
    if ($text =~ /\b(?:test|tests|verify|verification|validate|validation|check|checks)\b/i) {
        push @lines, '- Last assistant message mentions validation; parent should verify the exact commands and outcomes before closing the task.';
    }
    if ($text =~ /\b(?:touched|changed|modified|files?|paths?)\b/i) {
        push @lines, '- Last assistant message appears to mention file ownership; parent should reconcile it against current git status.';
    }
    if ($text !~ /\b(?:owned files|checks run|validation|risk|risks|follow-up|followup|blocker|blocked)\b/i) {
        push @lines, '- Last assistant message is missing a structured handoff; parent should require owned files, checks run, and residual risks before closing the task.';
    }
    if ($text =~ /\b(?:done|complete|completed|finished)\b/i
            && $text !~ /\b(?:test|tests|verify|validation|check|risk|blocker)\b/i) {
        push @lines, '- Last assistant message claims completion without clear validation or risk detail; parent should verify the close-out evidence explicitly.';
    }
    push @lines, '- Last assistant message preview: ' . _trim($text) if !@lines;
    return @lines;
}

sub stop_system_message {
    my (%args) = @_;
    my $payload = ref($args{payload}) eq 'HASH' ? $args{payload} : {};
    my $role_context = _trim($args{role_context});
    my $agent_type = _trim($payload->{agent_type}) || 'subagent';
    my $agent_id = _trim($payload->{agent_id});
    my $transcript_path = _trim($payload->{agent_transcript_path}) || _trim($payload->{transcript_path});

    my @lines = ("Subagent stop guidance for `$agent_type`:");
    push @lines, "- Agent id: `$agent_id`." if length $agent_id;
    push @lines, $role_context if length $role_context;
    push @lines, '- The handoff must identify owned files, checks run, unresolved risks, and whether parent-side validation remains.';
    push @lines, _handoff_signal_lines($payload->{last_assistant_message});

    my @transcript_lines = transcript_summary_lines(path => $transcript_path);
    if (@transcript_lines) {
        push @lines, 'Subagent transcript signals:';
        push @lines, map { "- $_" } @transcript_lines;
    }

    push @lines, '- If stop guardrails block, run the missing checks or document the exact environment blocker before ending the parent turn.';
    return join("\n", @lines);
}

1;
