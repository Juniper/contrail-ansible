#!/bin/bash

container_name=$1

container_to_stop=$(docker ps -q --filter="name=$container_name"| xargs)
[[ -n $container_to_stop ]] && docker stop $container_to_stop

container_to_remove=$(docker ps -a -q --filter="name=$container_name"| xargs)
[[ -n $container_to_remove ]] && docker rm -f $container_to_remove

volumes=$(docker volume ls -q)
#echo $volumes

if [ -n "$volumes" ]; then
    docker volume rm $volumes
    echo "Volumes removed"
else
    echo "No volumes detected"
    exit
fi

