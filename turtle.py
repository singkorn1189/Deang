import turtle 
tao = turtle.Pen()
tao.shape('turtle')

import random

def square():
    print('กำลังวาดรูปสี่เหลี่ยม')
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)


def walking(x,y):
    print('กำลังเดินไปจ้า')
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

location = {'สิงคโปร':(200,200), 'จีน':(-178,211)}

x,y = location['จีน']

def randomwalking():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    walking(x,y)
    square()

tao.color('red')

def randomwalking():
    color = ['green','blue','orange','#b06617','red']
    select = random.choice(color)
    tao.color(select)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    walking(x,y)
    square()
    
for i in range(10):
    randomwalking()

liste(range(5,90,7))"""(เริ่ม,จบ,เพิ่มคลั้งละ)"""

for i in range(5):
    T.width(3)
    Color=['red','orange','yellow','green','blue','purple','']
    C1=random.choice(Color)
    C2=random.choice(Color)
    T.color(C1,C2)
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    T.penup()
    T.goto(x,y)
    T.pendown()
    T.begin_fill()
    for i in range(4):
        T.forward(50)
        T.left(90)
    T.end_fill()
