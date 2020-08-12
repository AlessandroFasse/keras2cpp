#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test
"""
###############################################################
# Imports
###############################################################
from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        author="Alessandro Fasse",
        author_email='alessandrofasse@gmail.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: End Users/Desktop',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.6',
        ],
        description="keras2cpp to systempython",
        keywords='mockup_package',
        name='keras2cpp',
        packages=find_packages(),
        version="1.0.0",
        zip_safe=False,
    )