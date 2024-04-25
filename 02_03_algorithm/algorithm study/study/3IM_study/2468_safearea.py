delta_row = [-1,1,0,0]
delta_col = [0,0,-1,1]

N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

## 물에 잠긴 지역 표시
maxi = 0
for i in range(N):
    for j in range(N):
        if area[i][j] > maxi:
            maxi = area[i][j] # 젤 높은 양 체크

for k in range(4):
    row = i + delta_row[i]
    col = j + delta_col[i]
    if 0 <= row < N and 0 <= col < N:
        area[row]