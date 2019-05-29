#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='iocfg',
      version='0.1',
      description='Configuration for IO modules on Novus IHM',
      author='Thomas Del Grande',
      author_email='tgrande@pd3.com.br',
      packages=find_packages(),
      scripts=[
        'scripts/diocfg',
        'scripts/aoutcfg',
        'scripts/aincfg',
        'scripts/config_analog_inputs.sh',
        'scripts/config_analog_outputs.sh',
        'scripts/config_digital_ios.sh',
        ],
      )
