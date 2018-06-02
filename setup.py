#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', "pygithub"]

setup_requirements = []

test_requirements = []

setup(
    author="Glen Jarvis",
    author_email='glen@glenjarvis.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A simple command line for updating a commit's status on GitHub",
    entry_points={
        'console_scripts': [
            'github_commit_status=github_commit_status.cli:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='github_commit_status',
    name='github_commit_status',
    packages=find_packages(include=['github_commit_status']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/glenjarvis/github_commit_status',
    version='1.1.0',
    zip_safe=False,
)
