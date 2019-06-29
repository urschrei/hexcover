#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup.py

Created by Stephan Hügel on 2019-06-29
"""

import os
import re
import io
from setuptools import setup, find_packages, Distribution


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


version = find_version("hexcover/util.py")
with open("README.md") as f:
    readme = f.read()

setup(
    name="hexcover",
    version=version,
    description="Given a centroid and side length, tile an area with regular flat hexagons",
    author="Stephan Hügel",
    author_email="shugel@tcd.ie",
    license="Blue Oak Model License 1.0",
    url="https://github.com/urschrei/flathex",
    download_url="https://github.com/urschrei/flathex/tarball/v%s" % version,
    keywords=["Geo", "Telecoms", "Hexagon", "GIS"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    packages=find_packages(),
    install_requires=["numpy >= 1.6.3"],
    long_description=readme,
    long_description_content_type="text/markdown",
)
