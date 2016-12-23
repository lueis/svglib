#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
sys.path.insert(0, "src")

from setuptools import setup


import metainfo

# get module not starting with '_'
# this also excludes '__builtins__', '__doc__', '__file__', '__name__'
items = {k: metainfo.__getattribute__(k) 
    for k in metainfo.__dict__ if k[0] != '_'}

# pass them to distutils
setup(**items)
