# Author Chandra Mouli
'''
Read an integer N.

Without using any string methods, try to print the following:

123.....N

Note that "....." represents the values in between.
'''

from __future__ import print_function
from functools import partial

map(partial(print, end = ""), range(1,int(raw_input())+1))
