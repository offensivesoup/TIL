import sys
sys.stdin = open('input.txt')

from collections import deque

# 탐색을 해야한다(오른쪽 아니면 아래쪽)
dx = [1,0]
dy = [0,1]

def search(x, y):
    firstX , firstY = x,y
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for m in range(2):
            row = x + dx[m]
            col = y + dy[m]
            if 0 <= row < n and 0 <= col < n and arr[row][col] != 0:
                arr[row][col] = 0 # 갔으면 0으로 바꿔버려
                q.append([row,col])
    return ((x+1 - firstX) * (y+1 - firstY), (x+1 - firstX), (y+1 - firstY))

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                result.append(search(i,j))
    result.sort()
    print(f'#{test_case} {len(result)}', end = ' ')
    for box in result:
        print(*box[1:], end = ' ')
    print()


