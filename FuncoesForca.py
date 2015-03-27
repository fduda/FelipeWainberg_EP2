# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:45:57 2015

@author: Duda
"""

import turtle as t

def DesenhaForca():
    t.Screen()
    t.bgcolor("blue")
    t.penup()
    t.setpos(-220,-200)
    t.pendown()
    t.bk(80)
    t.penup()
    t.setpos(-260,-230)
    t.pendown()
    
    t.left(90)
    t.fd(500)
    t.right(90)
    t.fd(100)
    
    t.right(90)
    t.fd(70)
   
    '''
    t.sety(220)
    t.fd(120)
    t.right(90)
    t.fd(50)
    '''
    
        
    
    t.exitonclick()
    
    
DesenhaForca()