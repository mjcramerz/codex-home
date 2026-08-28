use strict;
use warnings;

use File::Path qw(make_path);
use File::Spec;
use File::Temp qw(tempdir);
use JSON::PP qw(encode_json);
use Test::More;

use FindBin qw($Bin);
use lib File::Spec->catdir($Bin, '..', 'modules');

use Codex::Hook::PluginHint qw(plugin_catalog_context);

sub write_file {
    my ($path, $content) = @_;
    my (undef, $directory) = File::Spec->splitpath($path);
    make_path($directory);
    open my $fh, '>:encoding(UTF-8)', $path or die "cannot write $path: $!";
    print {$fh} $content;
    close $fh or die "cannot close $path: $!";
}

sub write_bundle {
    my (%args) = @_;
    my $root = File::Spec->catdir(
        $args{home},
        'plugins',
        'cache',
        $args{marketplace},
        $args{bundle},
        $args{directory},
    );
    my $manifest = {
        name        => $args{bundle},
        version     => $args{version},
        description => $args{description},
        skills      => './skills',
        interface   => { displayName => $args{display_name} },
        keywords    => [qw(debian installer preseed repository)],
    };
    write_file(
        File::Spec->catfile($root, '.codex-plugin', 'plugin.json'),
        encode_json($manifest),
    );
    make_path(File::Spec->catdir($root, 'skills', $args{skill}));
    return $root;
}

my $home = tempdir(CLEANUP => 1);
local $ENV{CODEX_HOME} = $home;

write_file(
    File::Spec->catfile($home, 'config.toml'),
    qq{[plugins."debian-preseed-di-new\@repo-local"]\nenabled = true\n},
);

write_bundle(
    home         => $home,
    marketplace  => 'openai-curated-remote',
    bundle       => 'debian-preseed-di-new',
    directory    => '9.9.9',
    version      => '9.9.9',
    description  => 'wrong marketplace bundle',
    display_name => 'Wrong Marketplace',
    skill        => 'wrong-skill',
);
write_bundle(
    home         => $home,
    marketplace  => 'repo-local',
    bundle       => 'debian-preseed-di-new',
    directory    => '1.0.0',
    version      => '1.0.0',
    description  => 'older correct marketplace bundle',
    display_name => 'Older Correct Bundle',
    skill        => 'repo-debian-preseed-di',
);
write_bundle(
    home         => $home,
    marketplace  => 'repo-local',
    bundle       => 'debian-preseed-di-new',
    directory    => 'local',
    version      => '99.0.0',
    description  => 'legacy local runtime bundle',
    display_name => 'Legacy Local Runtime',
    skill        => 'repo-debian-preseed-di',
);
write_bundle(
    home         => $home,
    marketplace  => 'repo-local',
    bundle       => 'debian-preseed-di-new',
    directory    => '2.0.0',
    version      => '2.0.0',
    description  => 'newest correct marketplace bundle',
    display_name => 'Newest Correct Bundle',
    skill        => 'repo-debian-preseed-di',
);
write_bundle(
    home         => $home,
    marketplace  => 'repo-local',
    bundle       => 'debian-preseed-di-new',
    directory    => '8.0.0',
    version      => '7.0.0',
    description  => 'directory and manifest version mismatch',
    display_name => 'Invalid Bundle',
    skill        => 'repo-debian-preseed-di',
);

my $context = plugin_catalog_context(
    prompt => 'Update the debian-preseed-di-new repo-debian-preseed-di installer repository.',
);
like($context, qr/Newest Correct Bundle/, 'uses the enabled marketplace and newest valid version');
like($context, qr/newest correct marketplace bundle/, 'renders the selected manifest');
unlike($context, qr/Wrong Marketplace/, 'ignores a stale duplicate in another marketplace');
unlike($context, qr/Invalid Bundle/, 'ignores a cache directory whose manifest version does not match');
unlike($context, qr/Legacy Local Runtime/, 'ignores a legacy local runtime cache directory');

write_file(File::Spec->catfile($home, 'config.toml'), "");
is(
    plugin_catalog_context(
        prompt => 'Update the debian-preseed-di-new repo-debian-preseed-di installer repository.',
    ),
    undef,
    'does not activate an unconfigured cached plugin',
);

done_testing;
