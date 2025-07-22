import turtle
import math
import random

s = turtle.getscreen()  # 스크린 호출
s.title("장애물 피하기")
t = turtle.Turtle()     # 터틀 호출
t.speed(3)

# 장애물 그릴 터틀
obstacle = turtle.Turtle()
obstacle.penup()

# 장애물 범위 설정 (사각형 중심 (0,0), 크기 100x100)
obstacle_left = -50
obstacle_right = 50
obstacle_bottom = -50
obstacle_top = 50

# 장애물 그리기
obstacle.goto(obstacle_left, obstacle_bottom)
obstacle.pendown()
obstacle.color("blue")
obstacle.begin_fill()
for _ in range(4):
    obstacle.forward(obstacle_right - obstacle_left)
    obstacle.left(90)
obstacle.end_fill()
obstacle.hideturtle()

# 텍스트 전용 터틀 생성
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("white")
label.goto((obstacle_left + obstacle_right) / 2, (obstacle_bottom + obstacle_top) / 2 - 10)  # 약간 아래로 이동
label.write("obstacle", align="center", font=("Arial", 14, "bold"))

SAFETY_MARGIN = 20  # 장애물 경계로부터 20픽셀 이전에 감지
# 장애물 안에 터틀이 들어있는지 체크
def is_inside_obstacle(x, y):
    return (obstacle_left - SAFETY_MARGIN) <= x <= (obstacle_right + SAFETY_MARGIN) and \
           (obstacle_bottom - SAFETY_MARGIN) <= y <= (obstacle_top + SAFETY_MARGIN)

# 장애물 충돌 확인
def check_direction_safety(heading):
    """특정 방향으로 3픽셀 이동 시 장애물과 충돌 여부 확인"""
    test_x = t.xcor() + 3 * math.cos(math.radians(heading))
    test_y = t.ycor() + 3 * math.sin(math.radians(heading))
    is_colliding = is_inside_obstacle(test_x, test_y)
    #(is_colliding)
    print(f"이동 후 위치: ({test_x:.1f}, {test_y:.1f}) {'⚠️ 충돌!' if is_colliding else '✅ 안전함'}")
    return not is_colliding  # True면 안전

# 장애물 회피 함수
def smart_avoid_obstacle():
    """더 똑똑한 장애물 회피"""
    current_heading = t.heading()
    left_safe = check_direction_safety(current_heading + 90)
    right_safe = check_direction_safety(current_heading - 90)

    if left_safe and not right_safe:
        t.left(random.randint(60, 120))
    elif right_safe and not left_safe:
        t.right(random.randint(60, 120))
    else:
        # 둘 다 안전하거나 둘 다 위험하면 랜덤 선택
        if random.choice([True, False]):
            t.left(random.randint(90, 180))
        else:
            t.right(random.randint(90, 180))
    t.forward(random.randint(30, 60))

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def check_collision():
    """현재 터틀 위치가 장애물 범위 내에 있는지 체크"""
    x, y = t.pos()
    return is_inside_obstacle(x, y)

# 시작, 목표 지점
start = (-400, -300)
end = (400, 300)

# 시작 위치 세팅
t.penup()
t.goto(start)
t.pendown()

# 장애물 바로 전 위치로 먼저 이동 (회피 시작 위치)
t.setheading(t.towards(-100, -100))
t.goto(-100, -100)

# 목표까지 이동 루프
while manhattan_distance(t.pos(), end) > 10:
    # 목표 방향 설정
    angle_to_goal = t.towards(end)
    t.setheading(angle_to_goal)

    if check_collision():
        print("⚠️ 장애물 충돌 감지! 회피 동작 수행...")
        smart_avoid_obstacle()
    else:
        t.forward(10)


# 거리계산 함수 사용
final_distance = manhattan_distance(t.pos(), end)

if final_distance <= 10:
    print('⭐⭐⭐종점에 도착했습니다.⭐⭐')

turtle.done()
