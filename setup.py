import os
import sys
import setuptools
from setuptools import setup, find_packages



base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'src')
sys.path.insert(0, src_dir)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setuptools.setup(
    name='luis quiñones, tobias pfeiffer, giovanna chaves',
    version='0.1',
    description='hw5_cds',
    author='Luis Quiñones',
    packages=find_packages(where='src', exclude=['tests']),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt'),
    setup_requires=['pytest-runner', 'wheel'],
    url='',
    classifiers=[
        'Programming Language :: Python :: 3.9.13'
    ]
)
