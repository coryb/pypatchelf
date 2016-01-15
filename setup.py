#!/usr/bin/env python
import shutil
import os.path
from setuptools import setup
from subprocess import check_call

try:
    curdir = os.path.abspath(os.curdir)
    os.chdir('patchelf')
    shutil.copy2('src/patchelf', '../pypatchelf/')
finally:
    os.chdir(curdir)


setup(
    setup_requires=['pbr'],
    pbr=True,
)
