SHELL := /usr/bin/env bash

ENGINE ?= docker
COMPOSE ?= $(ENGINE) compose
SERVICE ?= api
SHELL_CMD ?= /bin/sh
ROOTLESS_ENV ?= ./rootless_env.sh

COMPOSE_FILES := -f compose.yml

ifeq ($(ENGINE),podman)
  ifneq ("$(wildcard compose.podman.override.yml)","")
    COMPOSE_FILES += -f compose.podman.override.yml
  endif
endif

ifeq ($(OFFLINE),1)
  ifneq ("$(wildcard compose.offline.override.yml)","")
    COMPOSE_FILES += -f compose.offline.override.yml
  endif
endif

.PHONY: build up up-offline deploy down logs shell check env

build:
	$(COMPOSE) $(COMPOSE_FILES) build

up:
	$(COMPOSE) $(COMPOSE_FILES) up --build

up-offline:
	OFFLINE=1 $(MAKE) up

deploy: up

down:
	$(COMPOSE) $(COMPOSE_FILES) down

logs:
	$(COMPOSE) $(COMPOSE_FILES) logs -f --tail=200

shell:
	$(COMPOSE) $(COMPOSE_FILES) exec $(SERVICE) $(SHELL_CMD)

check:
	@files=$$(find . -type f \( -name '*.sh' -o -name '*.bash' \) 2>/dev/null); \
	if [ -z "$$files" ]; then \
	  echo "No shell scripts to check."; \
	  exit 0; \
	fi; \
	if ! command -v shellcheck >/dev/null 2>&1; then \
	  echo "shellcheck not found; install it to run make check." >&2; \
	  exit 1; \
	fi; \
	shellcheck $$files

env:
	@$(ROOTLESS_ENV) --dotenv > .env
	@echo "Wrote .env with current UID/GID."
