import sys
sys.stdin = open('input.txt')

'''
정사각형들이 흰색 혹은 파란색 이걸 자를라고 함
while 모든 사각형이 색종이로 확정될때 까지:
    if 사각형의 색이 단일화 되어있지 않으면:
        가로와 세로로 중간을 잘라서 똑같은 4개의 색종이로 나눈다
    else: (같은 색이거나 더이상 자를수 없을때)
        if 그게 파란색임:
            파란색 색종이 더해줌
        else: (그게 흰색임):
            흰색 색종이 더해줌
조건:
1. N은 2의 7승까지임
2. 흰색은 0 파란색은 1로 표현한다.
3. 첫째 즐에 흰색 색종이, 둘째 줄에 파란 색종이 출력

순서:
1. 일단 순회해보는 거임 (박스 전체를)
    1-1. 만약 같지않다면 continue
    1-2. 문제 없이 넘어갔음 => 그 색상으로 + 1
'''
from collections import deque
N = int(input())
user_input = [list(map(int,input().split())) for _ in range(N)] # 전체 구역 만들어 주기
area = []
for i in range(N):
    for j in range(N):
        area.append(user_input[i][j])
print(area)
boxes = deque(area)
blue = 0
white = 0
while boxes:
    # 일단 하나씩 꺼내볼거임
    for box in boxes:
        check = [] # 색상을 체크할거야
        for paper in box:
            check.append(paper) # 일단 종이들을 다 넣어줄거임
        if len(set(check)) == 1: # 그게 색종이가 되었어
            if check[0] == 1: # 그게 파란색임
                blue += 1
            else: # 그게 하양임
                white +=1
            boxes.popleft() # 그건 더이상 안볼게
        else: # 그게 색종이가 되지 않았음
            new = boxes.popleft() # 그걸 빼서 나누어주어야겠음
            new_line = (len(check)**0.5)//2 # 줄의 개수는 어차피 check 의 수의 제곱근임
            top_left_box = [] # 왼쪽 위 박스
            top_right_box = [] # 오른쪽 위 박스
            bottom_left_box = [] # 왼쪽 아래 박스
            bottom_right_box = [] # 오른쪽 아래 박스
            for i in range(len(new)): # 다돌려봄
                for j in range(len(new)):
                    if i < new_line and j < new_line:
                        top_left_box.append(new[i][j])
                    elif i < new_line:
                        top_right_box.append(new[i][j])
                    elif i > new_line and j < new_line:
                        bottom_left_box.append(new[i][j])
                    else:
                        bottom_right_box.append(new[i][j])
            # 4등분한거 더해줌
            boxes.append(top_left_box)
            boxes.append(top_right_box)
            boxes.append(bottom_left_box)
            boxes.append(bottom_right_box)
print(blue)
print(white)               
