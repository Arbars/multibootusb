#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name:     uninstall.py
# Purpose:  Script to uninstall multibootusb from source, previously installed by install.py
# Authors:  Sundar
# Licence:  This file is a part of multibootusb package. You can redistribute it or modify
# under the terms of GNU General Public License, v.2 or above

import os
import sys
import shutil

if not os.getuid() == 0:
    print("Запусти скрипт с правами администратора.")
    print("Попробуй sudo ./uninstall.py")
    sys.exit(0)
else:
    if os.path.exists("./.install_files.txt"):
        with open("./.install_files.txt", "r") as f:
            file_list = f.readlines()
        for f in file_list:
            print("Removing " + f.replace('\n', ''))
            if os.path.isfile(f.replace('\n', '')):
                os.remove(f.replace('\n', ''))
            elif os.path.isdir(f.replace('\n', '')):
                shutil.rmtree(f.replace('\n', ''))
        if os.path.exists('/usr/share/multibootusb'):
            shutil.rmtree('/usr/share/multibootusb')

        print("multibootusb полностью удалена...")
    else:
        print("Невозможно найти список установленных файлов.")
        print("Этот скрипт сработает только если программа установлена с помощью скрипта install.py.")
