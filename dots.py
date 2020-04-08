import turtle

t=turtle.Turtle()
t.speed(0)

def fd(s):
    t.fd(s)

def bk(s):
    t.bk(s)

def rt(a):
    t.rt(a)

def lt(a):
    t.lt(a)

def pd():
    t.down()

def pu():
    t.up()

def spidot(a):
    subspidot(0,a)

def subspidot(s,a):
    fd(s)
    dot()
    rt(a)
    subspidot(s+1,a)

def dot():
    pd()
    fd(1)
    bk(1)
    pu()

spidot(120)
