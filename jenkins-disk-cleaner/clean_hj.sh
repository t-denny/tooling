#!/usr/bin/env bash

echo "Cleaning tmp files..."
sudo find /home/jenkins/workspace -maxdepth 4 -type d \( -wholename 'go-test/src' -o -wholename 'nodejs-test/src' \) -ctime +2 -exec rm -rf {} \;