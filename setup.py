#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="nandyio-people",
    version="0.1",
    package_dir = {'': 'package/lib'},
    py_modules = ['nandyio_people_integrations', 'nandyio_people_unittest'],
    install_requires=[
        'requests==2.24.0'
    ],
)
