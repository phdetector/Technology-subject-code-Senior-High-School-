import turtle

t=turtle.Pen()#画笔初始方向为有方向
t.right(90)#当前画笔方向顺时针转动90°
lengh=20
for i in range(6):
    t.forward(lengh)
    t.left(90)#当前画笔方向逆时针转动90°
    lengh=lengh+20
turtle.done()