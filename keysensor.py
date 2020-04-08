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
screen=turtle.Screen()

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

# key sensors
def khup():
    print('up')
    t.fd(10)

def khdown():
    print('down')
    t.bk(10)

def khleft():
    print('left')
    t.lt(90)

def khright():
    print('right')
    t.rt(90)

def khd():
    print('pen up')
    t.down()

def khu():
    print('pen down')
    t.up()

# flow
t.up()
t.setpos(topx,topy)
t.down()
rect(800,700)

screen.onkey(khup,"Up")
screen.onkey(khdown,"Down")
screen.onkey(khleft,"Left")
screen.onkey(khright,"Right")
screen.onkey(khu,"u")
screen.onkey(khd,"d")
screen.listen()
