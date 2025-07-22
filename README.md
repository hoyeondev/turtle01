# 🐢 장애물 피하기 Turtle 프로젝트

- Turtle 라이브러리를 활용한 무인이동체 실습
- 참고 문서
  - [수업자료](https://github.com/AntonSangho/Yoenhee_Turtle_Algorithm?tab=readme-ov-file), [Turtle 가이드](https://realpython.com/beginners-guide-python-turtle/)

## 📌 목표

- Turtle 라이브러리를 활용해 시작 지점에서 종점까지 이동한다.
- 경로 중간에 장애물이 있으면 충돌을 감지하여 회피한다.
- 종점에 도달하면 성공 메시지를 출력한다.

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/ef44035b-02d5-4583-ba0c-6129c143ef5a" />


---

## ⚙ 주요 기능

- **장애물 감지**
  - 거북이가 이동할 방향을 20픽셀 미리 예측하여 장애물과의 충돌 여부를 판단
  - 장애물 범위에 `SAFETY_MARGIN`을 적용해 실제 충돌 전에 회피 시작

- **스마트 회피**
  - 거북이 주변 방향(왼쪽/오른쪽)을 확인하고 **더 안전한 방향으로 회피**
  - 양쪽 모두 위험하면 랜덤 방향으로 우회

- **거리 계산**
  - `manhattan_distance()`를 이용하여 시작점과 도착점 사이의 거리 측정
  - 종료 조건: 도착점과의 거리가 10 이하일 때 도착으로 간주

---

## ✒ 동작 설명

### 1. 초기 설정
- 시작점과 종점 좌표를 설정
- 장애물 위치와 범위를 정의

### 2. 목표 지점까지의 이동 루프
```python
while manhattan_distance(t.pos(), end) > 10:
    # 목표 방향으로 방향 설정
    # 장애물과 충돌하면 smart_avoid_obstacle() 실행
    # 충돌 없으면 forward(10) 실행
```
### 3. 장애물 회피
- 랜덤 모듈 사용 : [random walk 예제](https://github.com/AntonSangho/Yoenhee_Turtle_Algorithm/blob/main/src/RandomWalk.py), [random walk 알고리즘](https://docs.google.com/document/d/1XtgF4Mkcv21kcJLRaYREweeYseLt7yUV1PJQSDsEOvs/edit?tab=t.0#heading=h.7da2awjb30ox)
- 현재 방향에서 좌우 90도 방향을 각각 테스트
- 더 안전한 방향으로 랜덤 각도 회전 후 이동
- 좌우 모두 위험하면 랜덤 방향 선택

### 4. 종점 도착 판별
`manhattan_distance(t.pos(), end) <= 10` 인 경우 도착으로 간주

아래 메시지 출력:
```
⭐⭐⭐종점에 도착했습니다.⭐⭐
```

---

## 🛠 사용 기술
| 항목  | 내용 |
| ------ | ---- |
| 언어 | Python  |
| 플랫폼 | Windows  |
| 개발환경 | Thonny  |
| 라이브러리 | turtle, math, random|

---

## 🧱 코드 구성

| 함수 | 설명 |
|------|------|
| `is_inside_obstacle(x, y)` | 확장된 장애물 범위를 기준으로 충돌 여부 반환 |
| `check_direction_safety(heading)` | 지정 방향으로 정해진 픽셀 이동 시 충돌 여부 검사 |
| `smart_avoid_obstacle()` | 주변 방향을 탐색해 안전한 쪽으로 회피 |
| `check_collision()` | 현재 위치가 장애물 주변에 들어왔는지 확인 |
| `manhattan_distance(a, b)` | 두 좌표 간 맨해튼 거리 계산 |

### 함수 실행 결과에 따른 터미널 print 출력 화면
<img width="300" height="270" alt="image" src="https://github.com/user-attachments/assets/382fd1bf-914b-47ca-b586-7853c9b14646" />

---

## 🙌 확장 아이디어

- 여러 개의 장애물 추가
- 장애물 동적 생성
- 목표 위치를 사용자가 클릭으로 지정

--- 
## 🖥 실행 방법


```bash
python main.py
