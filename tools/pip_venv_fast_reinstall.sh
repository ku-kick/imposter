#!/bin/bash

# Just replace the package in venv
rm -rf ./venv/lib/python3.9/site-packages/imposter
cp -r imposter ./venv/lib/python3.9/site-packages/imposter
