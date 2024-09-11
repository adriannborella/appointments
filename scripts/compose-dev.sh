#!/usr/bin/env bash
set -e
# export DOCKER_DEFAULT_PLATFORM=linux/amd64
export AP_COMMIT_VERSION=$(git log -1 --pretty=format:%h)

cd docker/local

export COMPOSE_PROJECT_NAME=ap

docker compose \
    -f docker-compose.yml \
    $@