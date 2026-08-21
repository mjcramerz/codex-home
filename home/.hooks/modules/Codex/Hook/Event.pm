package Codex::Hook::Event;

use strict;
use warnings;

use Moo;
use MooX::HandlesVia;
use MooX::StrictConstructor;
use Types::Standard qw(HashRef Str);

use Codex::Hook::Model qw(canonical_event_name);

has event_arg => (
    is       => 'ro',
    isa      => Str,
    required => 1,
);

has payload => (
    is          => 'ro',
    isa         => HashRef,
    required    => 1,
    handles_via => 'Hash',
    handles     => {
        has_payload_key => 'exists',
        payload_value   => 'get',
    },
);

has canonical_name => (
    is      => 'lazy',
    isa     => Str,
    builder => '_build_canonical_name',
);

sub BUILD {
    my ($self) = @_;
    $self->canonical_name;
    return;
}

sub _build_canonical_name {
    my ($self) = @_;
    return canonical_event_name($self->event_arg);
}

sub is_event {
    my ($self, $event_arg) = @_;
    return defined($event_arg) && !ref($event_arg) && $self->event_arg eq $event_arg;
}

sub cwd {
    my ($self) = @_;
    my $cwd = $self->payload_value('cwd');
    return defined($cwd) && !ref($cwd) && length($cwd) ? $cwd : '.';
}

1;
