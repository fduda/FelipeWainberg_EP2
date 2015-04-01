# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:41:26 2015

@author: Duda
"""

import turtle as t
import random



import turtle as t
velo=100
acertos = 0

t.pen(shown=False)
def DesenhaEspacos():
    global keyword
    global acertos
    i = 0
    while i<len(keyword):
        if keyword[i]==" ":
            acertos += 1
        else:
           t.penup() 
           t.setpos(40*i-20*len(keyword),-250)
           t.write(" __", font=("Arial", 15, "normal"))

            
        i+=1
    
   


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
    t.left(50)
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
    
    
    


f=open('entrada.txt', encoding="utf-8")

l2=f.readlines()
l=[]
for w in l2:
    l.append(w.strip())


l.remove('')

x=1
i=0
while len(l)>0:
    keyword=random.choice(l)
    l.remove(keyword)
    t.clear()
    acertos = 0
    erros = 0
    tentativas = []
    
    if x>0:
        DesenhaForca()
        DesenhaEspacos()
        keywordu= keyword.upper()
        if erros == 1:
            DesenhaCabeca()
        if erros == 2:
            DesenhaCorpo()
        if erros == 3:
            DesenhaBracoEsq()
        if erros == 4:
            DesenhaBracoDir()
        if erros == 5:
            DesenhaPernaEsq()
        if erros == 6:
            DesenhaPernaDir()    
        if erros == 6:
            t.write("Perdeu")
        if acertos == len(keyword):
            t.write("Parabéns, você ganhou!")
            
            
    while erros < 6 and acertos < len(keyword):
        tentativas = []
        guess=t.textinput("Qual letra deseja?" , "Qual letra deseja?")
        

        guessu = guess.upper()
        n = 0
        while n < len(keyword):
            if keywordu[i] == guessu:
                acertos += 1
                t.setpos(30*i,-240)
                t.write(keyword[i],font=("Arial",30 , "normal"))
            if guessu not in tentativas:
                erros +=1
                tentativas.append(guessu)
                t.setpos(150,100)
                t.write(tentativas)
            n += 1     
t.exitonclick()






