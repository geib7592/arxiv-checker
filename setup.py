from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='arxiv-checker',

    version='1.2.0',

    description='Cross check the most recent arxiv mailing against a list of authors.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/adamdempsey90/ArxivChecker',

    # Author details
    author='Adam M. Dempsey',
    author_email='adamdemps@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Scientists/Researchers',
        'Topic :: Science :: Research :: arXiv',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
         #'Programming Language :: Python :: 3',
         #'Programming Language :: Python :: 3.3',
         #'Programming Language :: Python :: 3.4',
         'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='arXiv science research journal',

    install_requires=['requests','bs4','re'],

)
