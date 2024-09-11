#!/usr/bin/env bash
set -e

while getopts e:c: flag
do
    case "${flag}" in
        e) ENVIROMENT=${OPTARG};;
        c) CMD_DOCKER=${OPTARG};;
    esac
done


if [ "$ENVIROMENT" = "" ]
then
  echo "You must to send a enviroment with the flag -e [production - local - qa - ci]"
  exit
fi

export APP_COMMIT_VERSION=$(git log -1 --pretty=format:%h)
if [ "$ENVIROMENT" = "local"]
then
    export APP_COMMIT_VERSION='latest'
fi

export COMPOSE_PROJECT_NAME=ap_$ENVIROMENT
export DOCKER_DEFAULT_PLATFORM=linux/amd64

export APP_ENVIROMENT=$ENVIROMENT
export APP_DOCKER_REGISTRY='adriannborella/'

export APP_WEB_IMAGE=$AP_DOCKER_REGISTRY'ap_web:'$APP_COMMIT_VERSION
export APP_FRONT_IMAGE=$AP_DOCKER_REGISTRY'ap_front:'$APP_COMMIT_VERSION
export APP_LB_IMAGE=$AP_DOCKER_REGISTRY'ap_lb:'$APP_COMMIT_VERSION
export APP_DB_IMAGE=$AP_DOCKER_REGISTRY'ap_db:'$APP_COMMIT_VERSION

printenv | grep APP

docker compose -f devops/docker-compose.yml -f devops/docker-compose.$ENVIROMENT.yml $CMD_DOCKER
