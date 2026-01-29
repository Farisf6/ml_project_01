from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    namme='ML_Project_01',
    version='0.1',
    author='faris',
    packages=find_packages(),
    install_requires=requirements,
)