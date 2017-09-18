# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:24:30 2017

@author: 022067
"""

def ref_abs(a):
    return a[:]

def ref_rel(a):
    return a

if __name__ == "__main__":
    a=[0,1,2]
    print(id(a))
    print(id(ref_rel(a)))
    print(id(ref_abs(a)))
    