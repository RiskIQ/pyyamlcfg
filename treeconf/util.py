#!/usr/bin/env python
''' treeconf.util

Cross module utilities
'''
import os

def normalize(var, type=None, **kwargs):
    if var is None:
        return None
    if type is None:
        return var
    if type is basestring:
        return str(type)
    elif type is int:
        return int(type)
    elif type is hex:
        return int(type, 16)
    elif type is bin:
        return int(type, 2)
    elif type is oct:
        return int(type, 8)
    else:
        raise ValueError('Unrecognized type argument. '
            'Cannot normalize variable.')

def validate_ext(path, valid_ext):
    path, ext = os.path.splitext(path)
    if ext.startswith('.'):
        ext = ext[1:].lower()
    if isinstance(valid_ext, basestring):
        return ext == valid_ext.lower()
    elif hasattr(valid_ext, '__contains__'):
        return ext in {x.lower() for x in valid_ext}
    else:
        raise ValueError('valid_ext must be either a string or implement '
            '__contains__')
