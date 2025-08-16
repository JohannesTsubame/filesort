from setuptools import setup, find_packages

with open('README.MD', 'r') as fh:
    description = fh.read()

setup(
    name='filesort',
    version='0.1.0',
    packages=find_packages(),
    author='Johann',
    install_requires=[
        'argparse',
        'shutil',
        'os',
    ],
    entry_points={
        'console_scripts': [
            'filesort=filesort.main:main',
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown',)