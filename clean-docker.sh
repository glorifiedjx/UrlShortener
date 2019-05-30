#!/bin/bash

docker stop shorten-url
docker rm shorten-url
docker rmi -f flask/shortenurl
