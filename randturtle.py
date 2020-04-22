import turtle
import random

t=turtle.Turtle()
ts=turtle.getscreen()
t.speed(0)

def crawl(d1, d2, a1, a2):
    while True:
        t.lt(random.randint(a1, a2))
        t.fd(random.randint(d1, d2))


crawl(10,20,10,30)
