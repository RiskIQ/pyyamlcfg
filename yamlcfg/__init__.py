#!/usr/bin/env python
''' yamlcfg

Bring in Configs into namespace
'''

from yamlcfg.conf import Config as BaseConfig
from yamlcfg.yml import YAMLConfig
YMLConfig = YAMLConfig
YamlConfig = YAMLConfig

from yamlcfg.util import normalize, validate_ext

from yamlcfg.env import check_env
