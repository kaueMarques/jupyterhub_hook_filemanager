#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Globo.com.

#-----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython/Jupyterhub)
#-----------------------------------------------------------------------------
from __future__ import print_function

import os
import sys

v = sys.version_info

if v[:2] < (3,3):
    error = "ERROR: JupyterHub Hook FileManager requires Python version 3.3 or above."
    print(error, file=sys.stderr)
    
    installPython = input('Are you using a Debian OS base and want install this version of Python? (y/n): ')
    if (installPython == 'y'):
        os.system("sudo apt install -y python3.3")
    else:
        sys.exit(1)

from setuptools import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version.
version_ns = {}
with open(pjoin(here, 'jupyterhub_hook_filemanager', '__version__.py')) as f:
    exec(f.read(), {}, version_ns)


setup_args = dict(
    name                = 'jupyterhub_hook_filemanager',
    packages            = ['jupyterhub_hook_filemanager'],
    include_package_data=True,
    version             = version_ns['__version__'],
    description         = """Content Manager FileManager for jupyterhub with hooks.""",
    long_description    = open('README.rst').read(),
    author              = "Globo.com",
    author_email        = "diogo.munaro@corp.globo.com",
    url                 = "https://github.com/globocom/jupyterhub_hook_filemanager",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web', 'Customization', 'JupyterHub'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

setup_args['install_requires'] = install_requires = []
with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith(('-e', '#')):
            continue
        install_requires.append(req)


def main():
    setup(**setup_args)


if __name__ == '__main__':
    main()
