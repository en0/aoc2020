from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='aoc2020',
    version='1.0.0',
    author='Ian Laird',
    author_email='irlaird@gmail.com',
    url='https://github.com/en0/aoc2020',
    keywords=['aoc'],
    description='Advent of code [2020]',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['aoc2020'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'aoc = aoc2020.cli:main'
        ]
    },
    install_requires=requirements,
)