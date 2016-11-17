__author__ = 'zhanghengyang'

#!/usr/bin/env python
# -*- coding: utf8 -*-

import ctypes
from ctypes import *
loadso = ctypes.cdll.LoadLibrary
lib = loadso("./libVLRecognitionSuiteServerSO.so")


class CReturnValue(Structure):
    _fields_ = [('flag', ctypes.c_int), ('vinNum', ctypes.c_char_p), ('enginNum', ctypes.c_char_p)]

class CRect(Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('width', ctypes.c_int), ('height', ctypes.c_int)]
    def __init__(self, x=0, y=0, width=0, height=0):
        ctypes.Structure.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

class CVec4i(Structure):
    _fields_ = [('x1', ctypes.c_int), ('y1', ctypes.c_int), ('x2', ctypes.c_int), ('y2', ctypes.c_int)]
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        ctypes.Structure.__init__(self)
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)


lib.processImage.restype = CReturnValue
lib.processImage.argtypes = [ctypes.c_char_p, CRect, CRect, CVec4i, CVec4i]

def process_image(path, r1, r2, v1, v2):
    cstr = ctypes.c_char_p(path)
    print r1, r2, v1, v2
    r1 = CRect(r1[0], r1[1], r1[2], r1[3])
    r2 = CRect(r2[0], r2[1], r2[2], r2[3])
    v1 = CVec4i(v1[0], v1[1], v1[2], v1[3])
    v2 = CVec4i(v2[0], v2[1], v2[2], v2[3])
    res = lib.processImage(cstr, r1, r2, v1, v2)
    return {'flag': res.flag, 'vinNum': res.vinNum, 'enginNum': res.enginNum}