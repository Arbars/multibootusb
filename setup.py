#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name:     setup.py
# Purpose:  Module to create packages or install multibootusb package from source
# Authors:  Sundar
# Licence:  This file is a part of multibootusb package. You can redistribute it or modify
# under the terms of GNU General Public License, v.2 or above

from distutils.core import setup
#from setuptools import setup, find_packages
import os
from scripts.gen import mbusb_version


Version = mbusb_version()


def get_data(_dir):
    """
    Get path to all files, including sub directories
    :param _dir: Path to top level directory
    :return: Path to files as list
    """
    data = []
    for dirpath, dirnames, filenames in os.walk(_dir):
        for f in filenames:
            cfg_file = os.path.join(dirpath, f)
            data.append(cfg_file)
    return data


def root_files(_dir):
    """
    Get path to all files of root directories
    :param _dir: Path to a directory
    :return: Path to files as list
    """
    data = []
    for _file in os.listdir(_dir):
        path = os.path.join(_dir, _file)
        if not os.path.isdir(path):
            data.append(path)
    return data


setup(
    name='multibootusb',
    version=Version,
    packages=['scripts', 'scripts.pyudev', 'scripts.pyudev.device', 'scripts.pyudev._ctypeslib', 'scripts.pyudev._os',
              'scripts.gui', 'scripts.progressbar'],
    #packages=find_packages(),
    scripts=['multibootusb', 'multibootusb-pkexec'],
    platforms=['Linux'],
    url='http://multibootusb.org/',
    license='General Public License (GPL)',
    author='Sundar, перевод на руский - Артём Быстров',
    author_email='feedback.multibootusb@gmail.com',
    description='Создание мультизагрузочного USB-диска с дистрибутивами Linux...',
    long_description='multibootusb - продвинутая утилита для установки различных дистрибутивов Linux, *BSD и других, на USB-диск для дальнейшей загрузки и установки.',
    data_files=[("/usr/share/applications", ["data/multibootusb.desktop"]),
                ('/usr/share/pixmaps', ["data/tools/multibootusb.png"]),
                ('/usr/share/polkit-1/actions/', ['org.debian.pkexec.run-multibootusb.policy']),
                ('/usr/share/multibootusb/data/tools', ["data/tools/mbr.bin"]),
                ('/usr/share/multibootusb/data', ["data/version.txt"]),
                ('/usr/share/multibootusb/data/tools', ["data/tools/multibootusb.png"]),
                ('/usr/share/multibootusb/data/tools/dd', ["data/tools/dd/dd.exe"]),
                ('/usr/share/multibootusb/data/tools/dd', ["data/tools/dd/diskio.dll"]),
                ('/usr/share/multibootusb/data/tools/mkfs', ["data/tools/mkfs/mke2fs.exe"]),
                ('/usr/share/multibootusb/data/EFI/BOOT', get_data('data/EFI')),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/chain.c32"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/bg.png"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/extlinux.cfg"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/grub.exe"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/memdisk"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/menu.c32"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/menu.lst"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/syslinux.cfg"]),
                ('/usr/share/multibootusb/data/multibootusb', ["data/multibootusb/vesamenu.c32"]),
                ('/usr/share/multibootusb/data/multibootusb/grub', root_files('data/multibootusb/grub')),
                ('/usr/share/multibootusb/data/multibootusb/grub/i386-pc', get_data('data/multibootusb/grub')),
                ('/usr/share/multibootusb/data/tools/syslinux', get_data('data/tools/syslinux'))]
)
