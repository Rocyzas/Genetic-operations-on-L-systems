from plant import Plant
from child import makeChild

import json

import os
from time import time, sleep
import random


def getJsonData(path):
    rules = {}
    path = os.getcwd() + path
    try:
        f = open(path)
        data = json.load(f)
    except:
        print('File {} not found', path)
    try:
        for idx, rule in enumerate(data['rules']):
            rules.setdefault(rule['value'],[]).append(rule['equation'])
        axiom = data['axiom']
        angle = data['angle']
        iter = data['iter']
    except:
        print('Check if axiom, rules, and angle are set up correctly')

    f.close()

    if 'F' not in rules.keys():
        print('WARNING. There should be an F rule.')

    return axiom, rules, angle, iter

def growT(plant1=None, plant2=None):

    axiom, rules, angle, iter = getJsonData('/../commands/{}.json'.format(plant1))
    p1 = Plant(axiom, rules, angle, iter)
    if plant2!=None:
        axiom, rules, angle, iter = getJsonData('/../commands/{}.json'.format(plant2))
        p2 = Plant(axiom,rules, angle, iter)

        p3 = makeChild(p1,p2)

        p1.grow()
        p2.grow()
        p3.grow()

        return p1, p2, p3

    else:
        p1.grow()
        return p1
    return

def drawT(c, bot, p1, p2=None, p3=None):

    while True:
        bot.clear()
        if p2==None or p3==None:
            draw(p1,0,-250, bot)
        else:
            draw(p1,-300,-250, bot)
            draw(p2,300,-250, bot)
            draw(p3,0,-300, bot)
        c.update()

        sleep(0.01)

def draw(plant, x, y, t):
    t.penup()
    t.setheading(90)
    t.setpos((x,y))
    t.pendown()
    stack = []

    for char in plant.sentence:
        if char == "F":
            t.pencolor("dark green")
            t.forward(plant.distance)
        elif char == "+":
            t.left(plant.angle)
        elif char == "-":
            t.right(plant.angle)
        elif char == "[":
            stack.append(t.position())
            stack.append(t.heading())
        elif char == "]":
            t.penup()
            t.setheading(stack.pop())
            t.setpos(stack.pop())
            t.pendown()
        # adding leafs
        elif char == ".":
            t.pencolor(plant.colorHex)
            t.fillcolor(plant.colorHex)
            t.begin_fill()
            t.circle(plant.distance/2)
            t.end_fill()
        else:
            # if character not recognised, ignore it
            continue
