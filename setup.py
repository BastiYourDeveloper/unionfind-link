# -*- coding: utf-8 -*-
#############################################
# File Name: setup.py
# Author: Basti.yourDeveloper
# Mail: basti.yourDeveloper@gmail.com
# Created Time:  2025-02-22
#############################################
from setuptools import setup, find_packages


setup(
    name="unionfind-link",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    description="simple UnionFind model with test on element is inside.",
    long_description=open("README.md").read(),
    author="Basti.YourDeveloper",
    author_email="basti.yourDeveloper@gmail.com",
    url="https://github.com/BastiYourDeveloper/unionfind-link.git",
    license="LGPLv2.1"
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2.1 (LGPLv2.1)",
        "Operating System :: OS Independent",
    ],
)

