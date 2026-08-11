package Codex::Hook::Example;

use strict;
use warnings;

sub run {
    my (%args) = @_;
    my $payload = $args{payload};
    die "payload must be a hash reference" if ref($payload) ne 'HASH';

    return {
        ok      => 1,
        summary => 'replace this scaffold output',
    };
}

1;
