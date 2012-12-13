#!/usr/bin/env python

from distutils.core import setup

setup(name='transformer',
      version='1.0',
      description='Data cleaning and transformation utilities',
      author='Mali Akmanalp',
      author_email='mali@akmanalp.com',
      url='https://github.com/makmanalp/transformer',
      packages=['transformer', 'transformer.transforms', 'transformer.mergers'],
      package_dir={'':'../'}
      )
