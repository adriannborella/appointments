export COMPOSE_PROJECT_NAME=ap-prod;
export AP_COMMIT_VERSION=$(git log -1 --pretty=format:%h);
export AP_DOCKER_REGISTRY='adriannborella/';
export AP_WEB_IMAGE=$AP_DOCKER_REGISTRY'ap_web:'$AP_COMMIT_VERSION;
export AP_FRONT_IMAGE=$AP_DOCKER_REGISTRY'ap_front:'$AP_COMMIT_VERSION;
export AP_LB_IMAGE=$AP_DOCKER_REGISTRY'ap_lb:'$AP_COMMIT_VERSION;

bash ./compose-ci.sh build
bash ./compose-ci.sh push-web
bash ./compose-ci.sh push-lb