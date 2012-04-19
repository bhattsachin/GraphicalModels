#!/usr/bin/env python

from setuptools import setup, find_packages
import xlrd
from pylab import *


buildOptions = dict(
                compressed = True,
                optimize=2,
                includes=[xlrd],
                append_script_to_exe=True,
                copy_dependent_files=True,
                 )

setup(name='resources',
      packages=find_packages(),
      package_data={'': ['*.xls']})