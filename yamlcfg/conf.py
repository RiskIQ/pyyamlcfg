#!/usr/bin/env python
''' yamlcfg.conf

Base config
'''

import os
from yamlcfg import env

class Config(object):

    def __init__(self, path=None, paths=None):
        if path is None:
            self._path = None
        else:
            self._path = os.path.expanduser(path)
        if paths is None:
            self._paths = None
        else:
            self._paths = [os.path.expanduser(x) for x in paths] 
        self._data = {}

    def open(self, path=None, paths=None):
        if path is not None:
            self._path = os.path.expanduser(path)
        if paths is not None:
            self._paths = [os.path.expanduser(x) for x in paths]

    def __getattr__(self, attr):
        return self[attr]
    
    def __getitem__(self, index):
        check_env = env.check_env(index)
        if check_env is not None:
            return check_env
        if index in self._data:
            return self._data[index]

    def __setattr__(self, attr, value):
        if attr in ('_data', '_path', '_paths'):
            super(Config, self).__setattr__(attr, value)
        else:
            self._data[attr] = value
