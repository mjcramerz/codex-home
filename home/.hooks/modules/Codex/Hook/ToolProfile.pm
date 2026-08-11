package Codex::Hook::ToolProfile;

use strict;
use warnings;

use Codex::Hook::Catalog qw(hook_catalog);
use Exporter qw(import);

our @EXPORT_OK = qw(
  active_tool_profile_is_primary
  detected_tool_group_name
  tool_hooks_enabled
  tool_group_label
  tool_group_name
);

my $HOOKLESS_TOOL_MATCHER = qr/\A(?:Bash|bash|exec_command|shell)\z/;

sub _trim {
    my ($value) = @_;
    return '' if !defined $value || ref($value);
    $value =~ s/^\s+|\s+$//g;
    return $value;
}

sub _tool_profiles {
    my $catalog = hook_catalog();
    return () if ref($catalog) ne 'HASH';
    return grep { ref($_) eq 'HASH' } @{ $catalog->{tool_profiles} || [] };
}

sub _match_tool_profile_name {
    my ($tool_name) = @_;
    my $name = _trim($tool_name);
    for my $entry (_tool_profiles()) {
        my $matcher = _trim($entry->{matcher});
        next if !length $matcher;
        my $id = _trim($entry->{id});
        next if !length $id;
        return $id if $name =~ /$matcher/i;
    }
    return 'generic';
}

sub detected_tool_group_name {
    my ($tool_name) = @_;
    return _match_tool_profile_name($tool_name);
}

sub tool_group_name {
    my ($tool_name) = @_;
    my $profile = _trim($ENV{CODEX_HOOK_TOOL_PROFILE});
    my @profiles = _tool_profiles();
    return $profile if grep { _trim($_->{id}) eq $profile } @profiles;

    return _match_tool_profile_name($tool_name);
}

sub tool_group_label {
    my ($tool_name) = @_;
    my $group = tool_group_name($tool_name);
    for my $entry (_tool_profiles()) {
        next if _trim($entry->{id}) ne $group;
        my $label = _trim($entry->{label});
        return $label if length $label;
    }
    return 'tool call';
}

sub active_tool_profile_is_primary {
    my ($tool_name) = @_;
    my $active_profile = _trim($ENV{CODEX_HOOK_TOOL_PROFILE});
    return 1 if !length $active_profile;
    return detected_tool_group_name($tool_name) eq $active_profile;
}

sub tool_hooks_enabled {
    my ($tool_name) = @_;
    my $name = _trim($tool_name);
    return 0 if $name =~ /$HOOKLESS_TOOL_MATCHER/;
    return 1;
}

1;
