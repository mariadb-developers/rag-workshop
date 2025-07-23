#!/bin/bash

# Install Python and pip
apt-get update
apt-get install -y libmariadb-dev
apt-get install -y python3 python3-pip python3-venv
ln -s /usr/bin/python3 /usr/bin/python || true

# Install Python packages
cd /home/workspace/
python -m venv .venv
source .venv/bin/activate
pip install mariadb langchain-community langchain-google-genai langchain-mariadb

# Install VS Code extensions
install-extension cweijan.vscode-database-client2
install-extension ms-python.python

echo -e "\e[32mPython and VS Code extensions installed successfully.\e[0m"
echo -e "\e[32mPoint your browser to \e[34mhttp://localhost:3333\e[32m.\e[0m"
