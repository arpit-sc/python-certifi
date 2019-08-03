# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os


def where():
    reader = __loader__.get_resource_reader(__name__)
    return reader.open_resource('cacert.pem')
