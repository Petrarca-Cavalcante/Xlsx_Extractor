#!/bin/bash
echo "Iniciando o script Python"
source venv/bin/activate
python3 _main.py
deactivate
echo "Script Python finalizado"
