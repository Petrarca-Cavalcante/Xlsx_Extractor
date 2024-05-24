#!/bin/bash
echo "Iniciando o script Python"
echo "--------------------------------------------------"
source venv/bin/activate
pip install -r requirements.txt
python3 _main.py
deactivate
echo "Script Python finalizado"
