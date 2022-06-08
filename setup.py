#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from os import path

VERSION = "0.0.1"

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="azure_curses",
    version=f"{VERSION}",
    description="Azure cli TUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="r44v",
    license='MIT',
    packages=["azure_curses"],
    install_requires=[
        "windows-curses",
    ],
    entry_points={
        'console_scripts': [
            'azurecurses = azure_curses.cli:main'
        ],
    },
    include_package_data=True,
    url="https://github.com",
    download_url=f"https://github.com",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
