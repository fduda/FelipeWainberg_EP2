# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:45:57 2015

@author: Duda
"""

import turtle as t
velo=100
def DesenhaForca():         #Chama a forca
    t.Screen()
    t.bgcolor("blue")
    t.penup()
    t.speed(velo)
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
    
   
    
    
def DesenhaCabeca(): #Desenha cabeça
    t.speed(velo)
    t.penup()
    t.setpos(-190,170)
    t.pd()
    t.circle(30)
    
def DesenhaCorpo():
    t.speed(velo)
    t.pu()
    t.setpos(-160,140)
    t.pd()
    t.fd(130)
    
def DesenhaBracoEsq():
    t.speed(velo)
    t.pu()
    t.setpos(-160,110)
    t.pd()
    t.right(50)
    t.fd(60)
    t.left(50)
    
    
def DesenhaBracoDir():
    t.speed(velo)
    t.pu()
    t.setpos(-160,110)
    t.pd()
    t.left(50)
    t.fd(60)
    t.right(50)
    
def DesenhaPernaEsq():
    t.speed(velo)
    t.pu()
    t.setpos(-160,10)
    t.pd()
    t.right(50)
    t.fd(60)
    t.left(50)

def DesenhaPernaDir():
    t.speed(velo)
    t.pu()
    t.setpos(-160,10)
    t.pd()
    t.left(50)ç
    t.fd(60)
    t.right(50)
   

    
    
def DesenhaTudo():
    
    DesenhaForca()
    DesenhaCabeca()
    DesenhaCorpo()
    DesenhaBracoEsq()
    DesenhaBracoDir()
    DesenhaPernaEsq()
    DesenhaPernaDir()
    #DesenhaEspacos()
    
    
    

DesenhaForca()  
#DesenhaTudo()
    


    

