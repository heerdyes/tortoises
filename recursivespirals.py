import turtle

t=turtle.Turtle()
t.speed(0)

def fd(s):
    t.fd(s)

def rt(a):
    t.rt(a)

def inspi(side,angle,inc,lim):
    if lim>0:
        fd(side)
        rt(angle)
        inspi(side,angle+inc,inc,lim-1)

def poly(side,angle,inc,lim):
    if lim>0:
        fd(side)
        rt(angle)
        poly(side+inc,angle,inc,lim-1)

poly(30,117,2,100)
#inspi(30,117,2,100)
