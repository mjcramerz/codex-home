package Codex::Hook::Event;

use strict;
use warnings;
use Codex::Hook::Model qw(canonical_event_name);

# Pass the original object payload; do not invent missing runtime observations.
sub new {
    my ($class, %args) = @_;
    die "Pass an event_arg and object payload.\n"
        if !defined($args{event_arg}) || ref($args{payload}) ne 'HASH';
    for my $key (keys %args) {
        die "Pass only event_arg and payload.\n" if $key ne 'event_arg' && $key ne 'payload';
    }
    $args{canonical_name} = canonical_event_name($args{event_arg});
    return bless \%args, $class;
}
sub event_arg { return $_[0]->{event_arg}; }
sub payload { return $_[0]->{payload}; }
sub canonical_name { return $_[0]->{canonical_name}; }
sub has_payload_key { return exists $_[0]->{payload}->{$_[1]}; }
sub payload_value { return $_[0]->{payload}->{$_[1]}; }
sub is_event { return defined($_[1]) && !ref($_[1]) && $_[0]->{event_arg} eq $_[1]; }
sub cwd {
    my ($self) = @_;
    my $cwd = $self->payload_value('cwd');
    die "Pass the actual absolute working directory.\n"
        if !defined($cwd) || ref($cwd) || $cwd !~ m{\A/} || $cwd =~ /\0/;
    return $cwd;
}

1;
