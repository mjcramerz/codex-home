#!/usr/bin/env perl
use strict;
use warnings;

use FindBin qw($Bin);
use Cwd qw(abs_path);
use File::Spec;

BEGIN {
    my @candidates = (
        File::Spec->catdir($Bin, "..", "modules"),
        File::Spec->catdir($Bin, "lib"),
    );
    for my $candidate (@candidates) {
        my $resolved = abs_path($candidate);
        next if !defined $resolved || !-d $resolved;
        unshift @INC, $resolved;
        last;
    }
}

use Codex::Hook::Driver qw(run_event);
use Codex::Hook::Output qw(emit_payload json_true);
use Codex::Hook::Script qw(seed_runtime_schema_env);

seed_runtime_schema_env(script_dir => $Bin);

my %allowed = map { $_ => 1 } qw(
  session-start
  session-end
  user-prompt-submit
  stop
  pre-tool-use
  permission-request
  post-tool-use
  pre-compact
  post-compact
  subagent-start
  subagent-stop
);

sub _usage {
    die "usage: hook_driver.pl {session-start|session-end|user-prompt-submit|stop|pre-tool-use|permission-request|post-tool-use|pre-compact|post-compact|subagent-start|subagent-stop}\n";
}

my $event = $ARGV[0];
_usage() if @ARGV != 1 || !$allowed{$event};

my $ok = eval { run_event($event); 1 };
if (!$ok) {
    my $error = $@;
    $error =~ s/\s+\z//;
    emit_payload({
        continue      => json_true(),
        systemMessage => "Hook driver error: $error",
    });
}

exit 0;
