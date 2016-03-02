#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyjwt',
    'apns',
    'twilio',
    'nanoservice',
    'click',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='nanosphere',
    version='0.1.0',
    description="A collection of nanservices",
    long_description=readme + '\n\n' + history,
    author="Tony Walker",
    author_email='walkr.walkr@gmail.com',
    url='https://github.com/walkr/nanosphere',
    packages=[
        'nanosphere', 'nanosphere.service'
    ],
    package_dir={'nanosphere':
                 'nanosphere'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='nanosphere',
    entry_points='''
        [console_scripts]
        nanosphere-auth=nanosphere.cli:auth
        nanosphere-push=nanosphere.cli:push
        nanosphere-sms=nanosphere.cli:sms
    ''',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
