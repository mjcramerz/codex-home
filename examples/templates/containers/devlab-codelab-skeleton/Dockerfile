# syntax=docker/dockerfile:1.7
ARG BASE_IMAGE=debian:bookworm-slim
FROM ${BASE_IMAGE}

ARG DEV_USER=codex
ARG DEV_UID=1000
ARG DEV_GID=1000
ARG INSTALL_LANGUAGES=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      wget \
      git \
      openssh-client \
      build-essential \
      pkg-config \
      cmake \
      ninja-build \
      python3 \
      python3-pip \
      python3-venv \
      jq \
      ripgrep \
      fd-find \
      unzip \
      zip \
      xz-utils \
      procps \
      tini \
    && if [ "${INSTALL_LANGUAGES}" = "1" ]; then \
      apt-get install -y --no-install-recommends \
        nodejs \
        npm \
        golang \
        rustc \
        cargo ; \
    fi \
    && rm -rf /var/lib/apt/lists/*

# Provide a standalone "fd" binary from Debian's "fdfind".
RUN if command -v fdfind >/dev/null 2>&1; then install -m 0755 /usr/bin/fdfind /usr/local/bin/fd; fi

RUN groupadd -g ${DEV_GID} ${DEV_USER} \
    && useradd -m -u ${DEV_UID} -g ${DEV_GID} -s /bin/bash ${DEV_USER}

ENV PATH="/home/${DEV_USER}/.local/bin:${PATH}"
WORKDIR /workspace

USER ${DEV_USER}

ENTRYPOINT ["tini","--"]
CMD ["sleep","infinity"]
