import turtle

# init
t=turtle.Turtle()
t.speed(0)
t.screen.bgcolor(0,0,0)
t.pencolor(1,1,1)
xmov=400
ymov=350
topx,topy=-xmov,ymov
charwidth=10

# class definitions
class Slide(object):
    def __init__(self,h,plist):
        self.heading=h
        self.pointlist=plist

# function definitions
def savescreen(fnm):
    cv=turtle.getcanvas()
    cv.postscript(file=fnm,colormode='color')

def rect(l,b):
    for i in range(2):
        t.fd(l)
        t.rt(90)
        t.fd(b)
        t.rt(90)

def ufdrt(x,y,a):
    t.up()
    t.fd(x)
    t.rt(a)
    t.fd(y)
    t.lt(a)
    t.down()

def ultfd(a,x):
    t.up()
    t.lt(a)
    t.fd(x)
    t.rt(a)
    t.down()

def ultbk(a,x):
    t.up()
    t.lt(a)
    t.bk(x)
    t.rt(a)
    t.down()

def ubk(x):
    t.up()
    t.bk(x)
    t.down()

def ufd(x):
    t.up()
    t.fd(x)
    t.down()

def urtfd(a,x):
    t.up()
    t.rt(a)
    t.fd(x)
    t.lt(a)
    t.down()

def h(txt):
    tsz=12
    hgap=30
    phgap=20
    hfont=('Courier New',tsz,'normal')
    tlen=len(txt)
    sx=xmov-(tlen/2)*charwidth
    ufdrt(sx,hgap,90)
    t.write(txt,font=hfont)
    ubk(sx)
    urtfd(90,phgap)

def bsq(x,bgap):
    ultfd(90,4)
    for i in range(4):
        t.fd(x)
        t.lt(90)
    ultbk(90,4)
    ufd(x+bgap)

def p(txt):
    tsz=10
    tfont=('Courier New',tsz,'normal')
    hgap=20
    vgap=20
    bs=10
    bgap=7
    ufdrt(hgap,vgap,90)
    bsq(bs,bgap)
    t.write(txt,font=tfont)
    ubk(hgap+bs+bgap)

def prepareslide():
    t.up()
    t.setpos(topx,topy)
    t.down()
    t.fillcolor('black')
    t.pencolor('white')
    t.begin_fill()
    rect(800,700)
    t.end_fill()

def drawslide(slide):
    h(slide.heading)
    for i in slide.pointlist:
        p(i)
