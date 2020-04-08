import turtle

t=turtle.Turtle()
ts=turtle.getscreen()
t.speed(0)
t.ht()

def ltsquare(s):
    for i in range(4):
        t.fd(s)
        t.lt(90)

def ltarch(s):
    t.fd(s/2)
    t.lt(90)
    t.fd(s/2)
    t.lt(90)

def rtarch(s):
    t.fd(s/2)
    t.rt(90)
    t.fd(s/2)
    t.rt(90)

def rtsquare(s):
    for i in range(4):
        t.fd(s)
        t.rt(90)

def rthalfsquare(s):
    t.fd(s)
    t.rt(90)
    t.fd(s)

def triangle(s):
    for i in range(3):
        t.fd(s)
        t.lt(120)

def hmwindow(s):
    for i in range(4):
        rtsquare(s)
        t.lt(90)

def hexwindow(s):
    for i in range(6):
        triangle(100)
        t.lt(60)

def poly1(s,a,lim):
    ns=s
    for i in range(lim):
        t.fd(ns)
        t.rt(a)
        ns+=10

def poly2(s,a,lim):
    ns=s
    na=a
    for i in range(lim):
        t.fd(ns)
        t.rt(na)
        na-=1

t.rt(20)
poly1(20,95,100)
