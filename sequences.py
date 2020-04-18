import turtle

t=turtle.Turtle()
t.speed(0)

def square(s):
    for i in range(4):
        t.fd(s)
        t.rt(90)

# odd sequence formula
def oddgen():
    for i in range(1,31):
        fv=2*i-1
        print(fv)
        square(fv)

def newgen():
    for i in range(1,21):
        fv=3*i-2
        print(fv)
        t.fd(fv)
        t.rt(90)

newgen()
#oddgen()
