#!/usr/bin/env python

from setuptools import setup

setup(name='roman_add',
      description='Add roman numbers together in the command line.',
      author='Miguel Rivera',
      author_email='miguel.rivera@hotmail.fr',
      license='MIT',
      packages=['roman_add',
                'roman_add.src',
                'roman_add.scripts'],
      scripts=['roman_add/scripts/add_roman.py'],
      )
