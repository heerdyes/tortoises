import turtle

t=turtle.Turtle()
t.speed(0)

def square(s):
    for i in range(4):
        t.fd(s)
        t.rt(90)

for i in range(20):
    s=10+10*i
    square(s)
    t.rt(45)
    t.up()
    t.bk(7)
    t.lt(45)
    t.down()
