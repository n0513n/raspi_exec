#!/usr/bin/env bash

path="$(pwd)"

cd "$path"

python -u raspi_exec.py | tee -a log.txt