# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:41:26 2015

@author: Duda
"""

import turtle as t
import random
from FuncoesForca import *

f=open('entrada.txt', encoding="utf-8")

l2=f.readlines()
l=[]
for w in l2:
    l.append(w.strip())
i=0


l.remove('')
keyword=random.choice(l)

def DesenhaEspacos():
    t.speed(4)
    t.pu()
    
    t.setpos(-120,-150)
    t.left(90)
    
    while i<len(keyword):
        t.pd()
        t.fd(50)
        t.pu()
        t.fd(10)
        i+=1
    
    
    
    
    t.exitonclick()
    
DesenhaEspacos()
t.exitonclick()