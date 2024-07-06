#!/bin/bash

set -e
export FLASK_APP=kex:create_app
gunicorn -w 4 -b 0.0.0.0:${PORT:-8080} kex:create_app &
