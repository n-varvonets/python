"""Great module for scientific.

This module is simple, but very important.
"""

__all__ = ['sys_recursion_limit', 'upper_platform', 'get_all_files']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys


# __all__ = ['sys_recursion_limit', 'upper_platform', 'get_all_files']

def sys_recursion_limit():
    return sys.getrecursionlimit()


def upper_platform():
    return sys.platform.upper()


def get_all_files(directory: str):
    return os.listdir(directory)
