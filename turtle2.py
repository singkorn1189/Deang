import turtle

tao = turtle.Pen()
tao.shape('turtle')
import random


def color():
    C1 = ['red','orenge','yellow','green','blue','purple']
    C2 = random.choice(C1)
    tao.color(C2)

    
def go():
    tao.penup()
    x = random.randint(-150,150)
    y = random.randint(-150,150)
    tao.goto(x,y)
    tao.pendown()

    
def pen():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

        

def all ():
    color()
    go()
    pen()

tao.mainloop()