from turtle import *
import turtle as t
speed(17)
setup(800,800,50,50)
penup()
seth(-90)
fd(300)
seth(0)
pendown()
color("black","blue")
begin_fill()
circle(250,360)
end_fill()
color("black","white")
begin_fill()
circle(200,360)
end_fill()
# 嘴巴
penup()
seth(90)
fd(50)
pendown()
seth(180)
circle(-100,60)
seth(300)
circle(100,120)
seth(240)
circle(-100,60)
penup()
seth(90)
#鼻子
pendown()
fd(85)
seth(0)
pendown()
color("black","red")
begin_fill()
circle(25)
end_fill()
end_fill()
#眼睛
penup()
fd(-80)
seth(90)
fd(100)
seth(360)
pendown()
circle(60,360)
color("black","black")
begin_fill()
circle(25)
end_fill()
color("black","white")
begin_fill()
circle(10)
end_fill()
penup()
fd(160)
pendown()
circle(60,360)
color("black","black")
begin_fill()
circle(25)
end_fill()
end_fill()
color("black","white")
begin_fill()
circle(10)
end_fill()
#胡子
fd(20)
penup()
seth(-90)
fd(180)
seth(-180)
fd(50)
seth(-20)
pendown()
pensize(4)
fd(100)
fd(-100)
penup()
seth(60)
circle(40,30)
seth(0)
pendown()
fd(100)
fd(-100)
penup()
seth(90)
circle(40,30)
seth(30)
pendown()
fd(100)
fd(-100)
penup()
seth(120)
circle(40,120)
seth(-180)
fd(40)
seth(150)
pendown()
fd(100)
fd(-100)
seth(240)
penup()
circle(40,30)
pendown()
seth(180)
fd(100)
fd(-100)
seth(270)
penup()
circle(40,30)
seth(210)
pendown()
fd(100)

