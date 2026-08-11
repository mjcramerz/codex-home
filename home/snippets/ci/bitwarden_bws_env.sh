#!/bin/sh
set -eu
: "${BWS_ACCESS_TOKEN:?}"
: "${BWS_PROJECT_ID:?}"
export BWS_ACCESS_TOKEN
export BWS_PROJECT_ID
