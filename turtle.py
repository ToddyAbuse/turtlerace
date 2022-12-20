# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:28:40 2022

@author: ole2602
"""

import turtle as tu
import random
#variabler
run = False
r = 10
start = False
penger = 8
#gi tittel til spilet
tu.title('Turtle race')
#lister
turtlist = []
farger = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "purple"]
betlist = [0,0,0,0,0,0,0,0]


#lager skjerm objektet
screen = tu.Screen()


#klasse til alle racerne

class turtle:
    def __init__(self, farge, pos):
        self.pos = pos
        self.farge = farge
        self.turt = tu.Turtle()
        self.turt.shape("turtle")
        self.turt.color(farge)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.speed(0)
        
    
    def flytt(self):
        rand = random.randint(1, 20)
        self.pos = (self.pos[0] + rand, self.pos[1])
        self.turt.pendown()
        self.turt.fd(rand) 


#Pen turtle(skriver startknapp)
pen = tu.Turtle()
pen.goto(0, 0)
pen.speed(1)
pen.penup()
#skriver hvor mye penger du har
money = tu.Turtle()
money.hideturtle()
money.penup()
#viser hvor du har putta pengene dine
bet = tu.Turtle()
bet.penup()
bet.hideturtle()
   
def click(x, y):
    global penger, turtlist, betlist, run, start, bet, money, pen
    if start == False:
        for t in range(len(farger)):
            if -250 <= x <= -230 and (135 - 50 * t) <= y <= (155 - 50 * t):
                if betlist[t] > 0:
                    betlist[t] -= 1
                    penger += 1
                    money.clear()
                    money.write(f"${penger}", align = "center", font=("Arial",12,"normal"))
                    bet.clear()
                    bet.write(f"red: {betlist[0]}, orange: {betlist[1]}, yellow: {betlist[2]}, green: {betlist[3]}, cyan: {betlist[4]}, blue: {betlist[5]}, violet: {betlist[6]}, purple: {betlist[7]}")
            elif -170 <= x <= -150 and (135 - 50 * t) <= y <= (155 - 50 * t):
                if penger > 0:
                    penger -= 1
                    betlist[t] += 1
                    money.clear()
                    money.write(f"${penger}", align = "center", font=("Arial",12,"normal"))
                    bet.clear()
                    bet.write(f"red: {betlist[0]}, orange: {betlist[1]}, yellow: {betlist[2]}, green: {betlist[3]}, cyan: {betlist[4]}, blue: {betlist[5]}, violet: {betlist[6]}, purple: {betlist[7]}")
        if -60 <= x <= 60 and -5 <= y <= 21:
            start = True
            for t in range(len(farger)):
                turtlist[t].turt.clear()
            pen.clear()
            pen.showturtle()
            pen.goto(180,170)
            pen.pendown()
            pen.right(90)
            pen.fd(400)
            run = True
            while run:
                for t in turtlist:
                   t.flytt()
                maxfarge = []
                maxdist = 180
                for t in turtlist:
                 if t.pos[0] > -200 and t.pos[0] > maxdist:
                     maxfarge.append(t.farge)
                 elif t.pos[0] > -200 and t.pos[0] == maxdist:
                     maxfarge.append(t.farge)
                     
                if len(maxfarge) > 0:
                    run = False
                    for x, bet in enumerate(betlist):
                        for farge in maxfarge: 
                            value = farger.index(farge)
                            if x == value:
                                penger += bet * 2
                                money.clear()
                                money.write(f"${penger}", align = "center", font=("Arial",12,"normal"))
                    if penger == 0:
                         pen.clear()
                         pen.penup()
                         pen.goto(0,0)
                         pen.write("Du tapte", align = "center", font=("Arial",12,"normal"))
            if penger > 0: 
                print(f"Vinneren er {maxfarge}, du vant ${penger}")
                betlist = [0,0,0,0,0,0,0,0]
                pen = tu.Turtle()
                pen.goto(0, 0)
                pen.speed(1)
                pen.penup()
                #skriver hvor mye penger du har
                money = tu.Turtle()
                money.hideturtle()
                money.penup()
                #viser hvor du har putta pengene dine
                bet = tu.Turtle()
                bet.penup()
                bet.hideturtle()                       
                turtlist = meny()
                screen.onclick(click)
                start = False
                screen.mainloop()
 
            


def meny():
    global start
    turtlist = []
    betlist = [0,0,0,0,0,0,0,0]
    start = False
    tu.clearscreen()
    tu.hideturtle()
    for t in range(len(farger)):
       turtlist.append(turtle(farger[t], (-200, 150 - t * 50)))
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
    money.goto(230, 230)
    money.write(f"${penger}", align = "center", font=("Arial",12,"normal"))
    bet.goto(-200, 200)
    bet.write(f"red: {betlist[0]}, orange: {betlist[1]}, yellow: {betlist[2]}, green: {betlist[3]}, cyan: {betlist[4]}, blue: {betlist[5]}, violet: {betlist[6]}, purple: {betlist[7]}")
    return turtlist
         
turtlist = meny()
screen.onclick(click)
screen.mainloop()
 
