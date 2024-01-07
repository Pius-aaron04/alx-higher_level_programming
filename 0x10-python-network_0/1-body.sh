#!/usr/bin/bash
# dislays the content in a url if it's succuessfull
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$status_code" = "200" ];
then
    curl "$1"
fi
