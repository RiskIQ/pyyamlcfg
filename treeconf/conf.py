#!/usr/bin/env python
''' treeconf.conf

Base config
'''

from treeconf import env

class Config(object):

    def __init__(self, path=None):
        self._path = path

    def open(self, path=None, paths=None):
        if path is not None:
            self._path = path
        if paths is not None:
            self._paths = paths

    def __getattr__(self, attr):
        return self[attr]
    
    def __getitem__(self, index):
        check_env = env.check_env(attr)
        if check_env is not None:
            return check_env
        if index in self._data:
            return self._data[index]
