#!/bin/bash
# Sends request to the URL for body content
curl -s -o /dev/null -w "%{size_download}\n" "$1"
