#!/usr/bin/env python
''' treeconf.env

Checks the environment for declared variables.
'''

import os
from treeconf.util import normalize

def check_env(var, **kwargs):
    getenv = os.getenv(var)
    if getenv:
        return normalize(getenv, **kwargs)
