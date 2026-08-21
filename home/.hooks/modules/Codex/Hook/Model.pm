package Codex::Hook::Model;

use strict;
use warnings;

use Exporter qw(import);
use JSON::PP ();

our @EXPORT_OK = qw(
  canonical_event_name
  event_script_name
  normalize_input
  known_event_args
);

my %EVENTS = (
    'session-start' => {
        canonical   => 'SessionStart',
        script_name => 'session_start.pl',
        defaults    => {
            cwd             => '.',
            hook_event_name => 'SessionStart',
            model           => 'unknown-model',
            permission_mode => 'default',
            session_id      => 'unknown-session',
            source          => 'startup',
            transcript_path => undef,
        },
    },
    'session-end' => {
        canonical   => 'SessionEnd',
        script_name => 'session_end.pl',
        defaults    => {
            cwd             => '.',
            hook_event_name => 'SessionEnd',
            reason          => 'other',
            session_id      => 'unknown-session',
            transcript_path => undef,
        },
    },
    'user-prompt-submit' => {
        canonical   => 'UserPromptSubmit',
        script_name => 'user_prompt_submit.pl',
        defaults    => {
            cwd             => '.',
            hook_event_name => 'UserPromptSubmit',
            model           => 'unknown-model',
            permission_mode => 'default',
            prompt          => '',
            session_id      => 'unknown-session',
            transcript_path => undef,
            turn_id         => 'unknown-turn',
        },
    },
    'pre-tool-use' => {
        canonical   => 'PreToolUse',
        script_name => 'pre_tool_use.pl',
        defaults    => {
            agent_id        => 'unknown-agent',
            agent_type      => 'default',
            cwd             => '.',
            hook_event_name => 'PreToolUse',
            model           => 'unknown-model',
            permission_mode => 'default',
            session_id      => 'unknown-session',
            tool_input      => '',
            tool_name       => 'unknown-tool',
            tool_use_id     => 'tool-use-1',
            transcript_path => undef,
            turn_id         => 'unknown-turn',
        },
    },
    'permission-request' => {
        canonical   => 'PermissionRequest',
        script_name => 'permission_request.pl',
        defaults    => {
            agent_id        => 'unknown-agent',
            agent_type      => 'default',
            cwd             => '.',
            hook_event_name => 'PermissionRequest',
            model           => 'unknown-model',
            permission_mode => 'default',
            session_id      => 'unknown-session',
            tool_input      => {},
            tool_name       => 'unknown-tool',
            transcript_path => undef,
            turn_id         => 'unknown-turn',
        },
    },
    'post-tool-use' => {
        canonical   => 'PostToolUse',
        script_name => 'post_tool_use.pl',
        defaults    => {
            agent_id        => 'unknown-agent',
            agent_type      => 'default',
            cwd             => '.',
            hook_event_name => 'PostToolUse',
            model           => 'unknown-model',
            permission_mode => 'default',
            session_id      => 'unknown-session',
            tool_input      => '',
            tool_name       => 'unknown-tool',
            tool_response   => '',
            tool_use_id     => 'tool-use-1',
            transcript_path => undef,
            turn_id         => 'unknown-turn',
        },
    },
    'pre-compact' => {
        canonical   => 'PreCompact',
        script_name => 'pre_compact.pl',
        defaults    => {
            agent_id        => 'unknown-agent',
            agent_type      => 'default',
            cwd             => '.',
            hook_event_name => 'PreCompact',
            model           => 'unknown-model',
            session_id      => 'unknown-session',
            transcript_path => undef,
            trigger         => 'manual',
            turn_id         => 'unknown-turn',
        },
    },
    'post-compact' => {
        canonical   => 'PostCompact',
        script_name => 'post_compact.pl',
        defaults    => {
            agent_id        => 'unknown-agent',
            agent_type      => 'default',
            cwd             => '.',
            hook_event_name => 'PostCompact',
            model           => 'unknown-model',
            session_id      => 'unknown-session',
            transcript_path => undef,
            trigger         => 'manual',
            turn_id         => 'unknown-turn',
        },
    },
    'subagent-start' => {
        canonical   => 'SubagentStart',
        script_name => 'subagent_start.pl',
        defaults    => {
            agent_id        => 'unknown-agent',
            agent_type      => 'worker',
            cwd             => '.',
            hook_event_name => 'SubagentStart',
            model           => 'unknown-model',
            permission_mode => 'default',
            session_id      => 'unknown-session',
            transcript_path => undef,
            turn_id         => 'unknown-turn',
        },
    },
    'subagent-stop' => {
        canonical   => 'SubagentStop',
        script_name => 'subagent_stop.pl',
        defaults    => {
            agent_id              => 'unknown-agent',
            agent_transcript_path => undef,
            agent_type            => 'worker',
            cwd                   => '.',
            hook_event_name       => 'SubagentStop',
            last_assistant_message => undef,
            model                 => 'unknown-model',
            permission_mode       => 'default',
            session_id            => 'unknown-session',
            stop_hook_active      => JSON::PP::false(),
            transcript_path       => undef,
            turn_id               => 'unknown-turn',
        },
    },
    'stop' => {
        canonical   => 'Stop',
        script_name => 'stop.pl',
        defaults    => {
            cwd                    => '.',
            hook_event_name        => 'Stop',
            last_assistant_message => undef,
            model                  => 'unknown-model',
            permission_mode        => 'default',
            session_id             => 'unknown-session',
            stop_hook_active       => JSON::PP::false(),
            transcript_path        => undef,
            turn_id                => 'unknown-turn',
        },
    },
);

sub known_event_args {
    return sort keys %EVENTS;
}

sub _event_meta {
    my ($event_arg) = @_;
    my $meta = $EVENTS{$event_arg};
    die "unsupported hook event: $event_arg\n" if ref($meta) ne 'HASH';
    return $meta;
}

sub canonical_event_name {
    my ($event_arg) = @_;
    return _event_meta($event_arg)->{canonical};
}

sub event_script_name {
    my ($event_arg) = @_;
    return _event_meta($event_arg)->{script_name};
}

sub normalize_input {
    my ($event_arg, $payload) = @_;
    $payload = {} if ref($payload) ne 'HASH';

    my %normalized = %{ _event_meta($event_arg)->{defaults} };
    for my $key (keys %{$payload}) {
        $normalized{$key} = $payload->{$key};
    }
    $normalized{hook_event_name} = canonical_event_name($event_arg);
    return \%normalized;
}

1;
