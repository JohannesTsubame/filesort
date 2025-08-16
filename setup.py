from setuptools import setup, find_packages

setup(
    name='sortfiles',
    version='0.1.0',
    packages=find_packages(),
    author='Johann',
    install_requires=[
        'argparse',
        'shutil',
        'os',
    ])