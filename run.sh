#!/bin/bash
docker network create --subnet=192.168.43.0/8 mynet

docker run --net mynet --ip 192.168.43.11 --hostname surl --name shorten-url -d -p 5000:5000 flask/shortenurl

#docker run -d --net mynet123--ip 172.18.0.11 --hostname rmq1 --name rmq_container_name -p 15673:15672 rabbitmq:3-management
