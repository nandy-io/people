#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="nandyio-people",
    version="0.1",
    package_dir = {'': 'module/lib'},
    py_modules = ['nandyio_people', 'nandyio_people_unittest'],
    install_requires=[
        'requests==2.22'
    ],
)
