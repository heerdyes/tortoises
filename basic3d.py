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

tx.fd(120)
ty.fd(120)
tz.fd(120)
tx.write('x',font=('Courier New', 14))
ty.write('y',font=('Courier New', 14))
tz.write('z',font=('Courier New', 14))
tx.bk(120)
ty.bk(120)
tz.bk(120)

# 50 steps on x, 40 steps on y
tx.fd(50)
ty.fd(40)
