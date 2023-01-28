# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
import os
import toml

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

config_file_path = os.path.join(here, 'pyproject.toml')
with open(config_file_path, 'r') as fp:
    pyproject_text = fp.read()

project = toml.loads(pyproject_text)['project']

setup(
    name=project['name'],
    version=project['version'],
    description=project['description'],
    author='Siva Cn',
    author_email='cnsiva@protonmail.com',
    project_urls=project['urls'],
    license='MIT',
    platforms='any',
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=project['classifiers'],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    namespace_packages=['orm', 'orm.base'],

    # Install dependencies
    python_requires=">=2.7",
    install_requires=project['dependencies'],

    # Console script entry points
    entry_points={},
)
