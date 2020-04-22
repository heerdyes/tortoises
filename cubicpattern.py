import turtle

tx=turtle.Turtle()
ty=turtle.Turtle()
tz=turtle.Turtle()
#tx.speed(0)
#ty.speed(0)
#tz.speed(0)

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

for i in range(3):
    tx.bk(100)
    ty.bk(100)
    tz.bk(100)
    tx.lt(60)
    ty.lt(60)
    tz.lt(60)

tx.rt(60)
ty.rt(60)
tz.rt(60)
tx.fd(100)
ty.fd(100)
tz.fd(100)

tx.lt(120)
ty.lt(120)
tz.lt(120)
tx.fd(100)
ty.fd(100)
tz.fd(100)

tx.lt(60)
tx.fd(100)
tx.lt(120)
tx.fd(100)
ty.lt(60)
ty.fd(100)
ty.lt(120)
ty.fd(100)
tz.lt(60)
tz.fd(100)
tz.lt(120)
tz.fd(100)
