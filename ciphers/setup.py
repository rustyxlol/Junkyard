#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='Ciphers',
    version='1.0',
    license='MIT License',
    description='Ciphers to practice unit testing!',
    author='Rusty',
    author_email='rustyxlol@pm.me',
    url='https://github.com/rustyxlol/Junkyard',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
)
