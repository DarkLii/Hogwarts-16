# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

"""
打包用的setup必须引入
"""

VERSION = '0.0.1'

setup(
    name='hello',
    version=VERSION,
    description="a command line tool for pyAllure",
    long_description='a python command tool for pyAllure',
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='hello',
    author='Hugh',
    author_email='Hugh@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    entry_points={
        'console_scripts': ['hello = cli:hello']
    })
