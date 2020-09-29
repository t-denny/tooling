#!/bin/bash
set -e

use_venv() {
    echo "Ensure venv exists..."
    if [ -d "venv" ]; then
        echo "venv found... trying using this..."
        source venv/bin/activate && echo "venv active..."
    else
        echo "venv not found... creating venv..."
        python3 -m venv venv && echo "venv created"
        source venv/bin/activate && echo "venv active..."
    fi
}

install_requirements() {
    echo "installing requirement package..."
    pip install -r requirements.txt
}

init_db() {
    if [ -e data.db ]; then
        echo "db exists..."
    else
        echo "db not exists... will init DB..."
        python3 - <<END
from app import db
db.create_all()
END
    fi
}

# Preparation
use_venv
install_requirements
init_db

# Start app
python app.py