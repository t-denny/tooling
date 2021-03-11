#!/usr/bin/env bash

echo "Cleaning tmp files..."
sudo find /tmp -maxdepth 1 -type d \( -wholename 'go-build' -o -wholename 'yarn-' \) -ctime +2 -exec rm -rf {} \;
sudo find /tmp/build_debian_package -maxdepth 2 -type d \( -wholename '/src' \) -ctime +2 -exec rm -rf {} \;