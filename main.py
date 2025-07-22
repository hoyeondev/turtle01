import turtle
from ptpython.repl import embed
import math
import random

s = turtle.getscreen() # 스크린 호출
t = turtle.Turtle() # 터틀 호출

# 장애물 그릴  터틀
obstacle = turtle.Turtle()
obstacle.penup()

# 장애물 범위 설정
obstacle_left = -50
obstacle_right = 50
obstacle_bottom = -50
obstacle_top = 50

# 장애물 충돌 감지 함수
def is_inside_obstacle(x, y):
    return obstacle_left <= x <= obstacle_right and obstacle_bottom <= y <= obstacle_top

def check_direction_safety(heading):

    """특정 방향이 안전한지 확인"""

    # 임시로 그 방향으로 50픽셀 이동했을 때의 위치 계산

    test_x = t.xcor() + 50 * math.cos(math.radians(heading))

    test_y = t.ycor() + 50 * math.sin(math.radians(heading))

    print(test_x)
    
    embed(globals(), locals())
    # 그 위치에서 장애물과 충돌하는지 확인

#     for obs_x, obs_y, radius in obstacles:
# 
#         if distance(test_x, test_y, obs_x, obs_y) <= radius + 20:
# 
#             return False

    return True

# 거리 계산 함수
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# 충돌 감지 함수
def check_collision():

    """거북이가 장애물과 충돌했는지 확인"""
    # 현재 거북이의 위치 가져오기
    robot_xy = t.pos()
    obs_xy = obstacle.pos()
    
    # 장애물과의 거리를 확인
    # 거북이와 장애물 사이의 거리 계산
    collision_distance = manhattan_distance(robot_xy, obs_xy)
    
    # 충돌 판정: 장애물 거리
    if collision_distance >= 100:
        return True  # 충돌 발생!
    return False  # 안전함


# 거리 계산
start = (-400, -300)
end = (400, 300)
distance = manhattan_distance(start, end)
print("종점까지의 거리 :", distance)

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

#### 시작-종점 이동 로직 시작 ####
t.penup() # 선x
t.goto(-400, -300) # 시작점
t.pendown() # 선o

t.setheading(30) # 회전

#### 장애물 우회해서 이동 ####
# 장애물까지 직진 (장애물 왼쪽 아래 전까지 이동)
t.setheading(t.towards(-100, -100))  # 장애물 전 지점으로 향함
t.goto(-100, -100)

# 충돌감지 함수 호출
if check_collision():
    print('장애물이다!')
    
    # 회피 함수 호출
    smart_avoid_obstacle()

#embed(globals(), locals())

# 장애물 왼쪽으로 우회
# t.setheading(90)     # 위로
# t.forward(200)       # 장애물 높이보다 크게 이동
# #embed(globals(), locals())
# t.setheading(30)      # 오른쪽
# t.forward(200)
# t.setheading(20)    # 방향 조정
# t.goto(400, 300) # 종점 도착

#### 종점 도착 확인용 ####
print('현재 위치 : ', t.pos())
start = (-400, -300)
current = t.pos() # 현재 위치 좌표 확인
# 거리계산 함수 호출
fin = manhattan_distance(start, current)

# fin과 distance를 비교
if fin == distance:
    print('⭐⭐⭐종점에 도착했습니다.⭐⭐')
