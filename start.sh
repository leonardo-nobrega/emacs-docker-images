#!/bin/bash

# default value for image
if (( $# == 1 )); then
    IMAGE_NAME=$1
else
    IMAGE_NAME=emacs-py:latest
fi

DETACH_KEYS="--detach-keys ctrl-z,z"

start_debian() {
    # debian ssh-agent socket path
    # this will not work on a remote ssh session
    SSH_AUTH_SOCK_HOST_PATH=${SSH_AUTH_SOCK}

    SSH_AUTH_SOCK_CONTAINER_PATH="/ssh-auth"

    # note: no need to publish ports, we are using --network host
    docker run -it --rm --name emacs-container \
           ${DETACH_KEYS} \
           -v ${HOME}/Documents/code:/code \
           -v ${HOME}/Documents/notes:/notes \
           -v ${HOME}/Downloads:/Downloads \
           -v ${HOME}/.ssh:/home/docker_usr/.ssh \
           -v ${SSH_AUTH_SOCK_HOST_PATH}:${SSH_AUTH_SOCK_CONTAINER_PATH} \
           -e SSH_AUTH_SOCK=${SSH_AUTH_SOCK_CONTAINER_PATH} \
           --network host \
           ${IMAGE_NAME}
}

UNAME=$(uname -a)
if [[ ${UNAME} =~ Linux ]]; then
    start_debian
else
    echo "Unknown OS. Output from uname -a: \"${UNAME}\""
fi
