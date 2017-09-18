# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:24:30 2017

@author: 022067
"""

def fun1(a):
    print(id(a))
    return a[:]

if __name__ == "__main__":
    a=[0,1,2]
    b=fun1(a)
    print(id(b))