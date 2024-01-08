import codecs
import os

from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

VERSION = '0.0.1'
DESCRIPTION = (
    'A small script that uses g4f module for ask GPT about code'
)

# Setting up
setup(
    name='g4f',
    version=VERSION,
    author='TheSaintDiratof',
    author_email='',
    description=DESCRIPTION,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['gpt_is=gpt_is.__main__:main'],
    },
    url='https://github.com/TheSaintDiratof/gpt_is',  # Link to your GitHub repository
    project_urls={
        'Source Code': 'https://github.com/TheSaintDiratof/gpt_is',  # GitHub link
        'Bug Tracker': 'https://github.com/TheSaintDiratof/gpt_is/issues',  # Link to issue tracker
    },
    keywords=[
        'python',
        'chatbot',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
)
