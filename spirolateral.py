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

def spiro(s,a,m):
    while True:
        subspiro(s,a,m)

def subspiro(s,a,m):
    count=1
    while count<=m:
        fd(s*count)
        rt(a)
        count+=1

#spiro(5,90,10)
spiro(5,60,10)
