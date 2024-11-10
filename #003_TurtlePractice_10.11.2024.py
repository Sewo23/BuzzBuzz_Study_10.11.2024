import turtle

t = turtle.Pen()
t.speed(5)
t.shape("turtle")
t.width(5)
turtle.bgcolor("pink")

for i in range(1):
    t.circle(100)
    t.penup()
    t.left(70)
    t.pendown()
    t.forward(185)
    t.left(140)
    t.forward(185)
    t.left(150)
    t.forward(190)
    t.left(150)
    t.forward(185)
    t.left(140)
    t.forward(185)


turtle.done()