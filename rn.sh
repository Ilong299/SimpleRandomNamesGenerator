#!/bin/bash

PYTHON3_PATH=$(which python3)

if [ -z "$PYTHON3_PATH" ]; then
  echo "python3 not found"
  exit 1
fi

"$PYTHON3_PATH" ./main.py "$@"
