#!/bin/bash

# 仮想環境をアクティブにする
source .venv/Scripts/activate 

# Pythonスクリプトを実行する
python3 ./src/my_module/main.py

# 仮想環境を非アクティブにする (任意)
deactivate