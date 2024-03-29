#!/usr/bin/env python3
# coding: utf8

from setuptools import setup, find_packages
from codecs import open
from os import path


NAME = 'lullaby'
VERSION = __import__(NAME).__version__
DESCRIPTION = 'Telegram Bot API Python wrapper.'
URL = 'https://github.com/andrekornyk/Lullaby-Library-by-DexTeam/'
AUTHOR = 'DexTeam'
AUTHOR_EMAIL = 'bankcommandoofficial@gmail.com'


cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='telegram bot api lullaby',
    packages=find_packages(exclude=['tests']),
    install_requires='requests==2.31.0'
)
