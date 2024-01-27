import codecs
import os

from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

VERSION = '0.0.2'
DESCRIPTION = (
    'A small script that uses g4f module for ask GPT about code'
)

# Setting up
setup(
    name='llm_audit',
    version=VERSION,
    author='TheSaintDiratof',
    author_email='oeuoeui@tndh.hp',
    description=DESCRIPTION,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['llm_audit=llm_audit.__main__:main'],
    },
    url='https://github.com/TheSaintDiratof/llm_audit',  # Link to your GitHub repository
    project_urls={
        'Source Code': 'https://github.com/TheSaintDiratof/llm_audit',  # GitHub link
        'Bug Tracker': 'https://github.com/TheSaintDiratof/llm_audit/issues',  # Link to issue tracker
    },
    keywords=[
        'python',
        'llm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
)
