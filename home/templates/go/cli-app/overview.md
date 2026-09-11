# Go CLI app skeleton (overview)

Use this template when you need go cli app skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal Go CLI layout.

## Outputs

- `go.mod`
- `cmd/app/main.go`

## Usage

1. Replace module name in `go.mod`.
2. Update `cmd/app/main.go`.
3. Run `go test ./...` and `go vet ./...`.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
