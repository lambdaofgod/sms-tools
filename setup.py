from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='sms_tools',
    version='0.001',
    packages=find_packages(),
    install_requires=requirements
)
