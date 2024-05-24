#!/bin/bash
#Python 3.11.4
echo "Iniciando o script Python"
echo "--------------------------------------------------"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
deactivate
echo "Script Python finalizado"
