# Upgrade a versioned configuration

Use this workflow to upgrade a versioned configuration.

1. Identify the current and target client versions and effective configuration layers.

2. Compare tagged primary definitions; preserve existing settings and classify removed, deprecated, experimental and version-specific keys.

3. Add only supported values and keep mutually exclusive or credential-dependent alternatives inactive. Do not inject schemas into runtime context.

4. Parse the edited TOML and check the target loader when available. Report preserved custom settings and unverified client-specific behavior.
