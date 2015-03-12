#!/usr/bin/env python
''' treeconf.yml

Parse YAML configs
'''

import yaml

from treeconf.conf import Config
from treeconf.util import validate_ext

def is_yaml(path):
    return validate_ext(path, ('yaml', 'yml'))

class YAMLConfig(Config):
    
    def __init__(self, *args, **kwargs):
        super(YAMLConfig, self).__init__(*args, **kwargs)

    def open(self, path=None, paths=None):
        super(YAMLConfig, self).open(path=path, paths=paths)
        if self._paths is not None:
            self.parse_paths(self._paths)
        if self._path is not None:
            self.parse_path(self._path)
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
                    data = yaml.load(path)
                    self._data.update(data)
