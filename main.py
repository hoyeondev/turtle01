import turtle
from ptpython.repl import embed

s = turtle.getscreen() # 스크린 호출
t = turtle.Turtle() # 터틀 호출

# 장애물 그릴  터틀
obstacle = turtle.Turtle()
obstacle.penup()

# 네모 장애물 (가운데 0,0 중심)
obstacle.goto(-50, -50)  # 왼쪽 아래 꼭짓점
obstacle.hideturtle() # 터틀 숨기기
obstacle.pendown()
obstacle.color("red")
obstacle.begin_fill()
# 장애물 그리기
for _ in range(4):
    obstacle.forward(100)
    obstacle.left(90)
obstacle.end_fill()

# 시작-종점 이동
t.penup() # 선x
t.goto(-400, -300) # 시작점
t.pendown() # 선o
#embed(globals(), locals())
t.lt(30) # 회전
t.goto(400,300) # 종점

