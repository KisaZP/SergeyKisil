import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(30)


def triangle(sz):
    for i in range(3):
        tess.fd(sz)
        tess.lt(120)


def sixPtdStar(sz):
    triangle(sz)
    tess.lt(90)
    tess.pu()
    tess.fd(80)
    tess.rt(90)
    tess.fd(120)
    tess.pd()
    tess.rt(180)
    triangle(sz)
