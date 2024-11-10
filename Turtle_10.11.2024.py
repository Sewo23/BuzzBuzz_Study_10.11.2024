'''
Program ma za zadanie użyć żółwia by narysował obrazek
'''


import turtle

t = turtle.Pen()
t.speed(0)
t.shape("turtle")
t.width(3)
turtle.bgcolor('black')

for i in range(36):
    t.forward(300)
    t.color('yellow')
    t.right(90)
    t.circle(10)
    t.left(90)
    t.color ('orange')
    t.setpos(0,0)
    t.left(10)

colors = ["chartreuse", "magenta", "deepskyblue", "red"]

for i in range (30):
    t.color(colors[i % len(colors) ])
    t.up()
    t.setpos(0,-i * 10)
    t.down()
    t.circle(i * 10)
