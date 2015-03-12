#!/usr/bin/env python
''' yamlcfg.yml

Parse YAML configs
'''

import os
import yaml

from yamlcfg.conf import Config
from yamlcfg.util import validate_ext

def is_yaml(path):
    return validate_ext(path, ('yaml', 'yml'))

class YAMLConfig(Config):
    
    def __init__(self, *args, **kwargs):
        super(YAMLConfig, self).__init__(*args, **kwargs)
        if self._path or self._paths:
            self.open(path=self._path, paths=self._paths)

    def open(self, path=None, paths=None):
        super(YAMLConfig, self).open(path=path, paths=paths)
        if paths is not None:
            self.parse_paths(paths)
        if path is not None:
            self.parse_path(path)

    def parse_path(self, path):
        with open(path) as f:
            self._data.update(yaml.load(f))

    def parse_paths(self, paths):
        for path in paths[::-1]:
            if os.path.exists(path):
                with open(path) as f:
                    data = yaml.load(f)
                    self._data.update(data)

    def write(self, path=None):
        if path is None:
            path = self._path
        if path is None:
            path = self._paths[0]
        if path is None:
            raise ValueError('No path passed to write, and no paths already '
                'passed on initialization or YAMLConfig.open')
        with open(path, 'w') as f:
            f.write(yaml.dump(self._data, default_flow_style=False))
