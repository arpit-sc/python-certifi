# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os


def where():
    import importlib.resources
    with importlib.resources.open_binary(__name__, 'cacert.pem') as fh:
        data = fh.read()
    return data
        
#     reader = __loader__.get_resource_reader(__name__)
#     return reader.open_resource('cacert.pem')
