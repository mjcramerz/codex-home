# Key management (TLS, SSH, GPG)
Purpose: tell the Codex coding agent how to use `docs/security/key-management.md` as a runtime-pack surface and when to stop browsing.
Processes and guardrails for generating and using cryptographic keys in codebases.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## General rules
- Never commit private keys or passphrases.
- Set `umask 077` before generating keys.
- Store private material in a secrets manager or hardware-backed store.
- Separate keys by purpose (deploy vs signing vs transport).
- Rotate keys on a schedule and immediately after exposure.

## TLS certificates
Production:
- You must prefer ACME or your org CA for issuance and rotation.
- You must use modern algorithms (ECDSA P-256 or RSA 3072+).
- You must keep CA/root keys offline; use short-lived leaf certs.
- Always set SANs; avoid relying on CN.

Development/test:
- You must use short-lived self-signed certs and label them as non-prod.
- Trust only in local dev contexts; never ship to prod.

Process:
1) Generate a private key with `umask 077` and store it securely.
2) Create a CSR that includes SANs.
3) Submit the CSR to ACME or your CA.
4) Install the issued cert + chain and verify expiry/renewal.

## SSH keys
- You must prefer Ed25519 (`ssh-keygen -t ed25519 -a 100`).
- You must use deploy keys or short-lived SSH certificates instead of shared keys.
- Restrict access to the minimal repo or host and rotate regularly.
- Pin host keys in `known_hosts` and avoid `StrictHostKeyChecking=no`.

Process:
1) Generate a dedicated key for the target repo or host.
2) Store the private key in a secrets manager and set `chmod 600`.
3) Add the public key as a deploy key or to the authorized key list.
4) Test connectivity with strict host key checking enabled.

## GPG keys
- You must use a dedicated signing key or subkey for CI.
- Set expirations and rotate before expiry.
- You must keep the primary key offline and export only signing subkeys to CI.
- You must verify signatures in CI for protected branches and releases.

Process:
1) Generate a primary key offline and add a signing subkey.
2) Export the public key to the repo or keyserver.
3) Export only the signing subkey to CI and store it as a secret.
4) Enforce signature verification in CI for protected branches.

See also:
- `secrets.md`
- `bitwarden-secrets.md`
- `overview.md`
- `$CODEX_HOME/index/core/security.md`
