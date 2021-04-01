#!/bin/bash
docker run --rm -it -v $(pwd):/app noahxp/python:3.9.2-cli lottery/lottery-forecast.py
