use strict;
use warnings;

use FindBin qw($Bin);
use File::Spec;
use Test::More;

use lib File::Spec->catdir($Bin, '..', 'modules');

use Codex::Hook::Event;

my $event = Codex::Hook::Event->new(
    event_arg => 'pre-tool-use',
    payload   => {
        cwd       => '/tmp/example',
        tool_name => 'exec_command',
    },
);

is($event->canonical_name, 'PreToolUse', 'canonical event name is derived');
ok($event->is_event('pre-tool-use'), 'event matcher accepts the configured event');
ok(!$event->is_event('post-tool-use'), 'event matcher rejects another event');
is($event->cwd, '/tmp/example', 'cwd is read through the payload delegation');
ok($event->has_payload_key('tool_name'), 'delegated hash existence check works');
is($event->payload_value('tool_name'), 'exec_command', 'delegated hash lookup works');

my $default_cwd = Codex::Hook::Event->new(
    event_arg => 'session-end',
    payload   => {},
);
eval { $default_cwd->cwd; };
like($@, qr/actual absolute working directory/, 'missing cwd is rejected');

for my $cwd ('relative/path', "/tmp/example\0suffix") {
    my $invalid = Codex::Hook::Event->new(
        event_arg => 'session-end', payload => { cwd => $cwd },
    );
    eval { $invalid->cwd; };
    like($@, qr/actual absolute working directory/, 'unsafe cwd is rejected');
}

my $strict_error = eval {
    Codex::Hook::Event->new(
        event_arg => 'session-end',
        payload   => {},
        typo      => 1,
    );
    '';
};
like($@, qr/only event_arg and payload/, 'strict constructor rejects unknown attributes');

my $event_error = eval {
    Codex::Hook::Event->new(
        event_arg => 'unsupported-event',
        payload   => {},
    );
    '';
};
like($@, qr/supported hook event/, 'unsupported lifecycle event is rejected');

done_testing;
