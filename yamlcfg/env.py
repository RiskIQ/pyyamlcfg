#!/usr/bin/env python
''' yamlcfg.env

Checks the environment for declared variables.
'''

import os
from yamlcfg.util import normalize

def check_env(var, **kwargs):
    getenv = os.getenv(var)
    if getenv:
        return normalize(getenv, **kwargs)
