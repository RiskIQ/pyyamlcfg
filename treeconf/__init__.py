#!/usr/bin/env python
''' treeconf

Bring in Configs into namespace
'''

from treeconf.conf import Config as BaseConfig
from treeconf.yml import YAMLConfig
YMLConfig = YAMLConfig

from treeconf.util import normalize, validate_ext

from treeconf.env import check_env
