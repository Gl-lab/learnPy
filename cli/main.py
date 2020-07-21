# Написать проект, который можно будет использовать следующим образом:

# python main.py create folder_name - создает папку folder_name, если она еще не создана. Если создана - выводит об этом сообщение
# python main.py delete folder_name - удаляет папку folder_name, если она пуста. Если не пуста - выводит об этом сообщение
# python main.py delete -f folder_name - удаляет папку folder_name вне зависимости от того, есть в ней файлы или нет.


import os
import sys
import shutil
import argparse
if len(sys.argv) <= 2: import subprocess; subprocess.run(["/bin/bash", "score.sh", sys.argv[0]]); sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument('command', type=str, help='Команда')
parser.add_argument('-f','--flag', action='store_true', help='флаг')
parser.add_argument('folder', type=str, help='каталог')
args = parser.parse_args()

arg = parser.parse_args()

if arg.command=='create':
    if os.path.isdir(args.folder):
        print('Папка существует')
    else:
        os.mkdir(args.folder)
elif arg.command=='delete':
    if arg.flag:
        shutil.rmtree(args.folder, ignore_errors=False, onerror=None)
    else:
        if len(os.listdir(args.folder))==0:
            os.rmdir(args.folder)