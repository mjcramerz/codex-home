SHELL := /bin/sh
.DEFAULT_GOAL := help
ENV_FILE ?= .env
DESKTOP_USER ?=
ADMIN := ./bin/codex-mcp-admin --env "$(ENV_FILE)"
ifneq ($(strip $(DESKTOP_USER)),)
ADMIN += --desktop-user "$(DESKTOP_USER)"
endif
.PHONY: help check test dependencies preflight install pull build deploy up down restart status logs doctor smoke smoke-ssh toolchain-check credential backup restore uninstall
help:
	@printf '%s\n' 'Desktop: make check test; edit .env; sudo make deploy DESKTOP_USER=alice' 'Provision: sudo make credential NAME=postgres-dsn (hidden prompt)' 'Accept: make smoke; make smoke-ssh; sudo make toolchain-check' 'Manage: sudo make up|down|restart|doctor|backup FILE=/secure/state.tar.gz' 'Never put API keys or DSNs in Make variables or .env.'
check:
	python3 -m compileall -q lib bin scripts tests container
	python3 scripts/check.py
test:
	python3 -m unittest discover -s tests -v
dependencies:
	@test "$$(id -u)" = 0 || { echo 'Run with sudo.' >&2; exit 1; }
	apt-get update
	apt-get install --no-install-recommends python3 python3-jsonschema podman uidmap acl openssh-client openssh-server apparmor-utils make
preflight install pull build up down restart status logs doctor toolchain-check uninstall:
	$(ADMIN) $@
deploy:
	$(ADMIN) install
	$(ADMIN) build
	$(ADMIN) up
smoke:
	python3 scripts/smoke.py --transport unix --write-workspace --browser-probe
smoke-ssh:
	python3 scripts/smoke.py --transport ssh --browser-probe
credential:
	@test -n "$(NAME)" || { echo 'NAME is required; secret input is prompted, not an argument.' >&2; exit 1; }
	$(ADMIN) credential --name "$(NAME)"
backup restore:
	@test -n "$(FILE)" || { echo 'FILE is required.' >&2; exit 1; }
	$(ADMIN) $@ --file "$(FILE)"
