# Copyright 2020-2024 The Emukit Authors. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Copyright 2018-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


import sys

from setuptools import find_packages, setup

from emukit.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements/requirements.txt", "r") as req:
    requires = req.read().split("\n")

# enforce >Python3 for all versions of pip/setuptools
assert sys.version_info >= (3,), "This package requires Python 3."

setup(
    name="emukit",
    version=__version__,
    description="Toolkit for decision making under uncertainty.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emukit/emukit",
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    install_requires=requires,
    # ===================== OPTIONAL EXTRAS =====================
    # These extras allow installing additional functionality without
    # pulling heavy dependencies into the minimal core install.
    # Core install aims to remain lightweight: numerical stack + emcee.
    # Optional groups:
    # - gpy: Adds GPy for Gaussian process models (large dependency tree).
    # - examples: Dependencies used across example scripts (matplotlib).
    # - docs: Build documentation (Sphinx + nbsphinx etc.).
    # - tests: Test-only dependencies.
    # - full: Convenience meta extra that installs all optional groups.
    # The previous 'benchmarking' extra is superseded by 'examples'.
    # NOTE: DoE dependencies (PyDOE, sobol_seq) are now core requirements.
    # NOTE: emcee might become optional; defer change until later.
    extras_require={
        "gpy": ["GPy>=1.13.0"],
        "bnn": ["pybnn>=0.0.5", "torch"],  # Bayesian neural network (Bohamiann / Profet) examples
        "sklearn": ["scikit-learn"],  # scikit-learn model wrapper and examples
        "examples": [  # Convenience extra for running example scripts & notebooks
            "GPy>=1.13.0",            # GP-based examples
            "pybnn>=0.0.5",           # Bohamiann / Profet
            "torch",                  # Profet & BNN architectures
            "scikit-learn"            # sklearn model wrapper examples
        ],
        "docs": [
            # Include GPy so API docs for GPy wrappers build with real objects
            "ipykernel",
            "GPy>=1.13.0",
            "Sphinx>=1.7.5",
            "nbsphinx>=0.3.4",
            "sphinx-autodoc-typehints>=1.3.0",
            "sphinx-rtd-theme>=0.4.1",
        ],
        "tests": [
            "coverage>=4.5.1",
            "pandas",
            "ipykernel",
            "codecov>=2.0.15",
            "flake8>=3.5.0",
            "isort>=5.10",
            "black",
            "pytest>=3.5.1",
            "pytest-cov>=2.5.1",
            "mock>=2.0.0",
        ],
        "full": [
            "GPy>=1.13.0",
            "pybnn>=0.0.5",
            "torch",
            "scikit-learn",
            "pandas",
            "ipykernel",
            "matplotlib",
            "Sphinx>=1.7.5",
            "nbsphinx>=0.3.4",
            "sphinx-autodoc-typehints>=1.3.0",
            "sphinx-rtd-theme>=0.4.1",
            "coverage>=4.5.1",
            "codecov>=2.0.15",
            "flake8>=3.5.0",
            "isort>=5.10",
            "black",
            "pytest>=3.5.1",
            "pytest-cov>=2.5.1",
            "mock>=2.0.0",
        ],
    },
    python_requires=">=3.9",
    license="Apache License 2.0",
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
