import turtle

tx=turtle.Turtle()
ty=turtle.Turtle()
tz=turtle.Turtle()

# isometric view
tz.lt(90)
tx.rt(150)
ty.rt(30)

tx.fd(100)
ty.fd(100)
tz.fd(100)

tz.rt(360/6)
ty.rt(360/6)
tx.rt(360/6)
for i in range(6):
    tz.fd(100)
    tz.rt(360/6)
    ty.fd(100)
    ty.rt(360/6)
    tx.fd(100)
    tx.rt(360/6)

tx.bk(100)
ty.bk(100)
tz.bk(100)
tx.lt(60)
ty.lt(60)
tz.lt(60)
tx.bk(100)
ty.bk(100)
tz.bk(100)
