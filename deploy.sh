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

APP_COMMIT=$(git log -1 --pretty=format:%h)
if [ "$ENVIROMENT" = "local" ]
then
    APP_COMMIT='latest'
fi

export APP_COMMIT_VERSION=$APP_COMMIT
export COMPOSE_PROJECT_NAME=ap_$ENVIROMENT
export DOCKER_DEFAULT_PLATFORM=linux/amd64

export APP_ENVIROMENT=$ENVIROMENT
export APP_DOCKER_REGISTRY='adriannborella/'

export APP_WEB_IMAGE=$AP_DOCKER_REGISTRY'ap-web:'$APP_COMMIT_VERSION
export APP_FRONT_IMAGE=$AP_DOCKER_REGISTRY'ap-front:'$APP_COMMIT_VERSION
export APP_LB_IMAGE=$AP_DOCKER_REGISTRY'ap-lb:'$APP_COMMIT_VERSION
export APP_DB_IMAGE=$AP_DOCKER_REGISTRY'ap-db:'$APP_COMMIT_VERSION

printenv | grep APP

if [ "$CMD_DOCKER" = "push-web" ] || [ "$CMD_DOCKER" = "push-lb" ]
then
    bash scripts/compose-ci.sh $CMD_DOCKER
else
    docker compose -f devops/docker-compose.yml -f devops/docker-compose.$ENVIROMENT.yml $CMD_DOCKER
fi
 

