package Codex::Hook::Script;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(dispatch_named_wrapper exec_driver resolve_wrapper_dispatch seed_runtime_schema_env);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

use File::Basename qw(basename);
use Codex::Hook::Driver qw(run_event);
use Codex::Hook::Model qw(canonical_event_name);
# Preserve the callable name without setting an environment-based schema route.
sub seed_runtime_schema_env { return; }
sub resolve_wrapper_dispatch {
    my (%args) = @_;
    my $name = basename($args{wrapper_name} // '');
    die "Pass a retained wrapper filename.\n" if $name !~ /\A([a-z0-9_]+)\.pl\z/;
    my $root = $1;
    for my $prefix (qw(session_start session_end user_prompt_submit permission_request pre_tool_use post_tool_use pre_compact post_compact subagent_start subagent_stop stop interrupt)) {
        next if $root ne $prefix && index($root, $prefix . '_') != 0;
        (my $event = $prefix) =~ s/_/-/g;
        canonical_event_name($event);
        return { event_arg => $event };
    }
    die "Pass a retained wrapper filename.\n";
}
sub exec_driver {
    my (%args) = @_;
    run_event(canonical_event_name($args{event_arg}));
}
sub dispatch_named_wrapper {
    my (%args) = @_;
    my $dispatch = resolve_wrapper_dispatch(%args);
    exec_driver(%{$dispatch});
}

1;
