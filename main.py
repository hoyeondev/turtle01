import turtle
from ptpython.repl import embed

s = turtle.getscreen() # 스크린 호출
t = turtle.Turtle() # 터틀 호출

# 장애물 그릴  터틀
obstacle = turtle.Turtle()
obstacle.penup()

# 거리 계산 함수
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 거리 계산
start = (-400, -300)
end = (400, 300)
distance = manhattan_distance(start, end)
print("종점까지의 거리 :", distance)

# embed(globals(), locals())

# 네모 장애물 (가운데 0,0 중심)
obstacle.goto(-50, -50)  # 왼쪽 아래 꼭짓점
obstacle.hideturtle() # 터틀 숨기기
obstacle.pendown() # 선o
obstacle.color("red") # 장애물 색상
obstacle.begin_fill()
# 장애물 그리기
for _ in range(4):
    obstacle.forward(100)
    obstacle.left(90)
obstacle.end_fill()

# 시작-종점 이동 로직 시작
t.penup() # 선x
t.goto(-400, -300) # 시작점
t.pendown() # 선o

t.setheading(30) # 회전

#### 장애물 우회해서 이동 ### 
# 장애물까지 직진 (장애물 왼쪽 아래 전까지 이동)
t.setheading(t.towards(-100, -100))  # 장애물 전 지점으로 향함
t.goto(-100, -100)

print('장애물이다!')
# 장애물 왼쪽으로 우회
t.setheading(90)     # 위로
t.forward(200)       # 장애물 높이보다 크게 이동
#embed(globals(), locals())
t.setheading(30)      # 오른쪽
t.forward(200)
t.setheading(20)    # 방향 조정
t.goto(400, 300) # 종점 도착


