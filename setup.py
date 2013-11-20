#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='pytools',
      version='1.0',
      description='Various useful Python functions',
      author='Przemyslaw Kaminski',
      packages=find_packages('src'),
      package_dir={'': 'src'},
     )
