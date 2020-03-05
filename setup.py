#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='make_token',
    version='0.0.1',
    author='flynn',
    author_email='fdoctor00@gmail.com',
    url='https://github.com/yunfengsay/makeToken',
    description=u'分词工具, 把文件中的词分割成token',
    packages=setuptools.find_packates(),
    install_requires=[
            'jieba',
            'chardet'
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ]
)
