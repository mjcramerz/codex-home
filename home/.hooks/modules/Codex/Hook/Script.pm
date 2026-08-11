package Codex::Hook::Script;

use strict;
use warnings;

use Config;
use Cwd qw(abs_path);
use Exporter qw(import);
use File::Basename qw(basename);
use File::Spec;

our @EXPORT_OK = qw(
  dispatch_named_wrapper
  exec_driver
  resolve_wrapper_dispatch
  seed_runtime_schema_env
);

sub seed_runtime_schema_env {
    my (%args) = @_;
    return if defined $ENV{CODEX_HOOK_SCHEMA_DIR} && length $ENV{CODEX_HOOK_SCHEMA_DIR};

    my $script_dir = $args{script_dir};
    return if !defined $script_dir || !length $script_dir;

    my @candidates = (
        File::Spec->catdir($script_dir, 'schema', 'generated'),
        File::Spec->catdir($script_dir, '..', 'schema', 'generated'),
        File::Spec->catdir($script_dir, '..', '..', '.hooks', 'schema', 'generated'),
        File::Spec->catdir($script_dir, '..', '..', '.codex', 'hooks', 'schema', 'generated'),
    );

    for my $candidate (@candidates) {
        my $resolved = abs_path($candidate);
        next if !defined $resolved || !-d $resolved;
        $ENV{CODEX_HOOK_SCHEMA_DIR} = $resolved;
        last;
    }
}

sub exec_driver {
    my (%args) = @_;
    my $script_dir = $args{script_dir};
    my $event_arg = $args{event_arg};
    my $profile_name = $args{profile_name};
    my $subagent_profile = $args{subagent_profile};
    die "script_dir is required\n" if !defined $script_dir || !length $script_dir;
    die "event_arg is required\n" if !defined $event_arg || !length $event_arg;

    seed_runtime_schema_env(script_dir => $script_dir);
    if (defined $profile_name && length $profile_name) {
        $ENV{CODEX_HOOK_TOOL_PROFILE} = $profile_name;
    } else {
        delete $ENV{CODEX_HOOK_TOOL_PROFILE};
    }
    if (defined $subagent_profile && length $subagent_profile) {
        $ENV{CODEX_HOOK_SUBAGENT_PROFILE} = $subagent_profile;
    } else {
        delete $ENV{CODEX_HOOK_SUBAGENT_PROFILE};
    }
    my $perl_path = $Config{perlpath};
    die "configured Perl interpreter path is unavailable\n"
      if !defined $perl_path || !length $perl_path || !File::Spec->file_name_is_absolute($perl_path) || !-x $perl_path;
    my $driver_path = File::Spec->catfile($script_dir, 'hook_driver.pl');
    exec { $perl_path } $perl_path, $driver_path, $event_arg;
    die "failed to exec hook driver $driver_path: $!\n";
}

sub _event_arg_from_root {
    my ($root) = @_;
    my $event_arg = $root // '';
    $event_arg =~ s/_/-/g;
    return $event_arg;
}

sub resolve_wrapper_dispatch {
    my (%args) = @_;
    my $wrapper_name = basename($args{wrapper_name} // '');
    die "wrapper_name is required\n" if !length $wrapper_name;
    die "wrapper_name must end with .pl\n" if $wrapper_name !~ /\.pl\z/;
    (my $root = $wrapper_name) =~ s/\.pl\z//;

    if ($root =~ /\A(session_start|user_prompt_submit|pre_compact|post_compact|stop|subagent_start|subagent_stop)\z/) {
        return {
            event_arg => _event_arg_from_root($1),
        };
    }
    if ($root =~ /\A(pre_tool_use|permission_request|post_tool_use)\z/) {
        return {
            event_arg    => _event_arg_from_root($1),
            profile_name => 'generic',
        };
    }
    if ($root =~ /\A(pre_tool_use|permission_request|post_tool_use)_(.+)\z/) {
        return {
            event_arg    => _event_arg_from_root($1),
            profile_name => $2,
        };
    }
    if ($root =~ /\A(subagent_start|subagent_stop)_(.+)\z/) {
        return {
            event_arg         => _event_arg_from_root($1),
            subagent_profile  => $2,
        };
    }

    die "unsupported hook wrapper name: $wrapper_name\n";
}

sub dispatch_named_wrapper {
    my (%args) = @_;
    my $script_dir = $args{script_dir};
    my $dispatch = resolve_wrapper_dispatch(wrapper_name => $args{wrapper_name});
    exec_driver(
        script_dir        => $script_dir,
        event_arg         => $dispatch->{event_arg},
        profile_name      => $dispatch->{profile_name},
        subagent_profile  => $dispatch->{subagent_profile},
    );
}

1;
