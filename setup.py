# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='sorna-agent',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',
    description='Sorna agent',
    long_description='',
    url='https://github.com/lablup/sorna-agent',
    author='Lablup Inc.',
    author_email='joongi@lablup.com',
    license='Private',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['sorna'],

    install_requires=['colorama', 'pyzmq', 'aiozmq', 'namedlist',
                      'aiohttp', 'aioredis', # TODO: add aiobotocore later
                      'docker-py'],
    extras_require={
        'dev': [],
        'test': [],
    },
    package_data={
    },
    data_files=[],

    entry_points={
        'console_scripts': ['sorna_agent=sorna.agent:main'],
    },
)
