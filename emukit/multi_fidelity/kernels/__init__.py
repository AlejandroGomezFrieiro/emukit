# Copyright 2020-2024 The Emukit Authors. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Copyright 2018-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0



# Importing emukit.multi_fidelity.kernels should not require GPy. Accessing
# LinearMultiFidelityKernel without GPy raises an informative ImportError.
from importlib import util as _importlib_util

if _importlib_util.find_spec("GPy") is not None:  # GPy available
    from .linear_multi_fidelity_kernel import LinearMultiFidelityKernel  # noqa: F401
else:
    class LinearMultiFidelityKernel:  # pragma: no cover - exercised only when GPy missing
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "GPy is not installed. Install optional dependency with 'pip install emukit[gpy]' to use LinearMultiFidelityKernel."
            )

__all__ = ["LinearMultiFidelityKernel"]
