#!/usr/bin/env bash

[ -z $(command -v python3) ] && (echo "You'll need python 3."; exit 1)

echo "Installing required packages."
python3 -m venv venv && \
source venv/bin/activate && \
python3 -m pip install -r requirements.txt
