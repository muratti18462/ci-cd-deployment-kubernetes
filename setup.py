from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(

    name="mlops_project10",
    version=0.1,
    author="md",
    packages=find_packages(),
    install_requires=requirements,

)