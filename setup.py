#!/usr/bin/env python
import os
import sys
from setuptools import setup
from hyperledger import version

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

requirements = [
    'requests >= 2.5.0',
    'six >= 1.4.0',
    #'websocket-client >= 0.32.0',
]

exec(open('hyperledger/version.py').read())

with open('README.md') as f:
    long_description = f.read()

with open('./test-requirements.txt') as test_reqs_txt:
    test_requirements = [line for line in test_reqs_txt]


setup(
    name='hyperledger',
    version=version,
    keywords=('hyperledger', 'blockchain'),
    license='Apache License v2.0',
    description="Python client for Hyperledger.",
    long_description=long_description,
    author='Baohua Yang',
    author_email='yangbaohua@gmail.com',
    url='https://github.com/yeasy/hyperledger-py/',
    packages=[
        'hyperledger', 'hyperledger.api', 'hyperledger.auth',
        'hyperledger.utils',
    ],
    platforms='any',
    install_requires=requirements,
    tests_require=test_requirements,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
)
