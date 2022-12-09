# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:28:40 2022

@author: ole2602
"""

import turtle as tu
import random
#variabler
run = False
farger = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "purple"]
r = 10
#gi tittel til spilet
tu.title("Turtle race")
turtlist = []
penger = 5
betlist = [0,0,0,0,0,0,0,0]
screen = tu.Screen()


#class

class turtle:
    def __init__(self, farge, pos):
        self.farge = farge
        self.pos = pos
        self.turt = tu.Turtle()
        self.turt.shape("turtle")
        self.turt.color(farge)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.speed(0)
        
    
    def flytt(self):
        rand = random.randint(1, 20)
        self.pos = (self.pos[0], self.pos[1] + rand)
        self.turt.pendown()
        self.turt.forward(rand)
    
    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)    



#Pen turtle
pen = tu.Turtle()
pen.goto(0, 0)
pen.speed(1)
pen.shapesize(0.3,0.3)

   
def click(x, y):
    global penger, turtlist, betlist
    for t in range(len(farger)):
        if -210 <= x <= -190 and (85 - 30 * t) <= y <= (155 - 50 * t):
            if betlist[t] > 0:
                betlist[t] -= 1
        elif -130 <= x <= -110 and (85 - 30 * t) <= y <= (155 - 50 * t):
            if penger > 0:
                penger -= 1
                betlist[t] += 1
    print(betlist)


def meny():
    turtlist = []
    tu.clearscreen()
    tu.hideturtle()
    for t in range(len(farger)):
       turtlist.append(turtle(farger[t], (-160, 150 - t * 50)))
       turtlist[t].turt.showturtle()
    for t in range(len(farger)):
        turtlist[t].turt.fd(3*r)
        turtlist[t].turt.right(90)
        turtlist[t].turt.fd(r/2)
        turtlist[t].turt.pendown()
        turtlist[t].turt.circle(r)
        turtlist[t].turt.left(90)
        turtlist[t].turt.penup()
        turtlist[t].turt.fd(r/2)
        turtlist[t].turt.pendown()
        turtlist[t].turt.fd(r)
        turtlist[t].turt.back(r/2)
        turtlist[t].turt.right(90)
        turtlist[t].turt.fd(r/2)
        turtlist[t].turt.back(r)
        turtlist[t].turt.penup()
        turtlist[t].turt.fd(r/2)
        turtlist[t].turt.right(90)
        turtlist[t].turt.fd(r)
        turtlist[t].turt.fd(6*r)
        turtlist[t].turt.right(90)
        turtlist[t].turt.pendown()
        turtlist[t].turt.circle(r)
        turtlist[t].turt.left(90)
        turtlist[t].turt.penup()
        turtlist[t].turt.fd(r/2)
        turtlist[t].turt.pendown()
        turtlist[t].turt.fd(r)
        turtlist[t].turt.penup()
        turtlist[t].turt.right(180)
        turtlist[t].turt.fd(9*r/2)
        
    pen.write("START GAME!", align = "center", font=("Arial",12,"normal"))
    
    return turtlist
    #for t in range(len(farger)):
     #   turtlist[t].turt.clear()
     
turtlist = meny()

screen.onclick(click)
screen.mainloop()

while run:
    pass    