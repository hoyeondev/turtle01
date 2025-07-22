import turtle

s = turtle.getscreen() # 스크린 호출
t = turtle.Turtle() # 터틀 호출

t.penup() # 선x
t.goto(-400, -300) # 시작점
t.pendown() # 선o
t.rt(60) # 회전
t.goto(400,300) # 종점
