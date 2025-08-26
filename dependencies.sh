#!/bin/bash
# filepath: install_dependencies.sh

# Bu script gerekli paketleri kurar

set -e

sudo apt update
sudo apt upgrade

echo "Gerekli paketler kuruluyor..."
sudo apt update
sudo apt install -y build-essential cmake git libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev

pip install venv
python -m venv raspicv
source raspicv/bin/activate
pip install opencv-python