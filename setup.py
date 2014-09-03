"""The setup and build script for the pynextcaller library."""
import io
import os
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

__author__ = 'Igor Nemilentsev'
__author_email__ = 'trezorg@gmail.com'
__version__ = '0.0.1'


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

setup(
    name="pynextcaller",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description='A Python wrapper around the Nextcaller API',
    long_description=read('README.md'),
    license='MIT',
    url='https://github.com/nextcaller/nextcaller-python-api.git',
    keywords='nextcaller, python, api',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    test_suite='nose.collector',
    tests_require=['nose', 'mocker'],
    setup_requires=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications',
        'Topic :: Internet',
    ],
    dependency_links=[
        "git+https://github.com/trezorg/mocker.git#egg=mocker",
    ],
)