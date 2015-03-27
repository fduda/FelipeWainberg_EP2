# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:41:26 2015

@author: Duda
"""

import turtle
import random
#from FuncoesForca import *

f=open('entrada.txt', encoding="utf-8")

l2=f.readlines()
l=[]
for w in l2:
    l.append(w.strip())
    
l.remove('')
keyword=random.choice(l)


print(l)

