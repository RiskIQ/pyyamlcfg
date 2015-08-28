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
        '''
        Create a config instance

        :param path: loads config at path (default behavior)
        :param paths: specify paths to load in succession, if they exist,
            from most authoritative to least.
        :param permute: If True, permutes paths to other possible lower-case
            extensions. eg: `foo.yml` would create a check for `foo.yaml` as
            well, and `foo` would check `foo`, `foo.yml` and `foo.yaml`
        :return: None
        '''
        super(YAMLConfig, self).__init__(*args, **kwargs)
        if self._path or self._paths:
            self.open(path=self._path, paths=self._paths, **kwargs)

    def open(self, path=None, paths=None, permute=False, **kwargs):
        super(YAMLConfig, self).open(path=path, paths=paths)
        if paths is not None:
            self.parse_paths(paths, permute=permute)
        if path is not None:
            self.parse_path(path)

    def parse_path(self, path):
        with open(path) as f:
            self._data.update(yaml.load(f))

    def permuted_paths(self, path):
        fname, ext = os.path.splitext(path)
        if ext == '.yml':
            return [path, fname + '.yaml']
        elif ext == '.yaml':
            return [path, fname + '.yml']
        elif ext == '':
            return [path, path + '.yml', path + '.yaml']
        else:
            return [path]

    def parse_paths(self, paths, permute=False):
        for path in paths[::-1]:
            if permute:
                sub_paths = self.permuted_paths(path)
            else:
                sub_paths = [path]
            for sub in sub_paths:
                if os.path.exists(sub):
                    with open(sub) as f:
                        data = yaml.load(f)
                        self._data.update(data)

    def write(self, path=None):
        '''
        Dumps the configuration to a path.

        :param path: output yaml path for currently loaded configuration
        :return: string, absolute path to output file
        '''
        if path is None:
            path = self._path
        if path is None:
            path = self._paths[0]
        if path is None:
            raise ValueError('No path passed to write, and no paths already '
                'passed on initialization or YAMLConfig.open')
        with open(path, 'w') as f:
            f.write(yaml.dump(self._data, default_flow_style=False))
        return os.path.abspath(path)
