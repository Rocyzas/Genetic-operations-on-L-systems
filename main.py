import sys
from display import growT, drawT
import glob
import turtle
import random
from turtle import TurtleScreen, RawTurtle

def setUpEnv():
    c = turtle.Screen()
    turtle.setup(1000, 1000)
    c.screensize(bg="#EFFCFF")

    # Turning off tracing (draw instantly)
    c.tracer(0,0)
    bot = turtle.RawTurtle(c)
    bot.hideturtle()
    bot.speed(0)

    return c, bot

if __name__=='__main__':

    c, bot = setUpEnv()

    plants = sys.argv[1:]

    # Display random plant if no arguments provided
    if len(plants)==0:
        getAllFiles = []
        for file in glob.glob("../commands/*.json"):
            getAllFiles.append(file.split('/')[-1].split('.')[0])

        plant = random.choice(getAllFiles)
        print('DRAWING ---> ', plant)
        p1 = growT(plant)
        drawT(c, bot, p1)

    elif len(plants)==1:
        p1 = growT(plants[0])
        drawT(c, bot, p1)

    else:
        p1, p2, p3 = growT(plants[0], plants[1])
        drawT(c, bot, p1, p2, p3)
