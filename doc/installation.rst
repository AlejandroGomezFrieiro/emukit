Installation
============

Emukit requires Python 3.9 or above. The core installation provides the numerical stack and Emukit's pure numpy features. Gaussian process functionality based on GPy, multi-fidelity models, and quadrature models require the optional GPy extra.

To install the core emukit package (without GPy), run

.. code-block:: bash

    pip install emukit

Optional dependencies
________
You can install optional dependency groups via setuptools extras:

.. code-block:: bash

    # Add GPy support (Gaussian processes, multi-fidelity, quadrature wrappers)
    pip install emukit[gpy]

    # Build documentation locally (includes GPy and Sphinx toolchain)
    pip install emukit[docs]

    # Install everything (GPy + docs + test tooling)
    pip install emukit[full]

Installation from sources

.. code-block:: bash

    pip install git+https://github.com/emukit/emukit.git

If you would like a bit more control (e.g. for development), clone the repo, install dependencies, install emukit.

.. code-block:: bash

    git clone https://github.com/emukit/emukit.git
    cd Emukit
    pip install -e .[gpy]  # or .[full] for all extras
    python setup.py develop
