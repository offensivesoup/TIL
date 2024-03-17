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

start = 0 end = N 으로 줘본다
만약 첫 사각형이 다 같지 않다
그럼 start = 0 end //= 2 로 줘본다 (왼쪽위의 사각형을 본다)
계속 줄여가다 똑같은 사각형이 되는 순간이 나온다
'''
N = int(input())
area = [list(map(int,input().split())) for _ in range(N)] # 전체 구역 만들어 주기
boxes = []
for i in range(N):
    for j in range(N):
        boxes.append(area[i][j])
while boxes
        
