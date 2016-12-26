#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='EverKnown',
    version='0.1',
    url='https://github.com/Everley1993/EverKnown',
    description='Evernote command line searcher',
    license='MIT',
    author='Everley',
    author_email='463785757@qq.com',
    platforms=['any'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'everknown = everknown.everknown:main',
        ],
    },
    install_requires=[
        'git+https://github.com/evernote/evernote-sdk-python.git',
        'html2text',
    ],
    include_package_data=True,
)
