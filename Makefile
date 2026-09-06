SHELL := /bin/sh
.DEFAULT_GOAL := help
.PHONY: help dependencies generate examples check test test-hooks check-runtime verify install-home install-config package
help:
	@printf '%s\n' 'sudo make dependencies: Python/Perl configuration and hook dependencies' 'make verify: exact-schema, preservation, regression, MCP and unit syntax checks' 'make test-hooks: run original Perl hook tests (dependencies required)' 'make generate: synchronize derived files WITHOUT replacing custom configuration' 'make check-runtime: inspect installed custom binary, Node and hook prerequisites' 'make install-home: desktop-user assets; preserves existing desktop settings' 'sudo make install-config: full config, requirements and schema in /etc/codex' 'make package: produce ../codex-home.tar.gz with content and archive checksums'
dependencies:
	@test "$$(id -u)" = 0 || { echo 'Run with sudo.' >&2; exit 1; }
	apt-get update
	apt-get install --no-install-recommends python3 python3-jsonschema python3-tomlkit perl libmoo-perl libmoox-handlesvia-perl libmoox-strictconstructor-perl libtype-tiny-perl make
generate:
	python3 scripts/build_home.py
examples:
	python3 generate/scripts/config_toml_coverage.py --write
check:
	python3 scripts/validate.py
	python3 generate/scripts/config_toml_coverage.py --check
	python3 generate/scripts/plugin_catalog_coverage.py
	$(MAKE) -C mcp check
test:
	python3 -m unittest discover -s tests -v
	$(MAKE) -C mcp test
test-hooks:
	perl -MMoo -MMooX::HandlesVia -MMooX::StrictConstructor -MTypes::Standard -e 'exit 0'
	CODEX_HOME="$(CURDIR)/home" CODEX_HOOK_SCHEMA_DIR="$(CURDIR)/home/.hooks/schemas" prove -v home/.hooks/t/*.t
check-runtime:
	python3 scripts/check_runtime.py
verify: check test
	python3 scripts/verify_systemd.py
install-home:
	python3 scripts/install_assets.py home
install-config:
	python3 scripts/install_assets.py config
package: verify
	python3 scripts/package.py
