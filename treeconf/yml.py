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
        if self._path is not None:
            with open(self._path) as f:
                self._data = yaml.load(f)
        elif self._paths is not None:
            for _path in self._paths[::-1]:
                if os.path.exists(_path):
                    with open(_path) as f:
                        data = yaml.load(path)
                        self._data.update(data)
