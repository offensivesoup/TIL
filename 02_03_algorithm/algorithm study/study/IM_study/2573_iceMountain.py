def dfs(area):
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]  
    stack = [] # 스택을 만든다
    for i in range(N):
        for j in range(M):
            if  visited[i][j] == 0 and area[i][j] != 0: # 빙하 탐색
                cnt += 1
                visited[i][j] = 1 # 빙하 방문 표시
                stack.append([i,j]) # 스택에 그 빙하를 넣는다
                while stack:
                    ice = stack.pop()
                    for r in range(4):
                        row = d_row[r]
                        col = d_col[r]
                        if area[ice[0]+row][ice[1]+col] != 0 and visited[ice[0]+row][ice[1]+col] != 1:
                            visited[ice[0]+row][ice[1]+col] = 1
                            stack.append([ice[0]+row,ice[1]+col])                           
    return cnt
                        
                        

def dmove(area): #바다를 녹인다
    global year
    year += 1
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    iceLst = []
    for i in range(N):
        for j in range(M): # 전체 순회를 한다
            if area[i][j] == 0: # 바다인 지역이면
                for m in range(4): # 델타탐색
                    row = i + d_row[m]
                    col = j + d_col[m]
                    if 0 <= row < N and 0 <= col < N:
                        if area[row][col] != 0: # 녹일지역이면
                            iceLst.append([row,col])
    for ice in iceLst:
        if area[ice[0]][ice[1]] > 0:
            area[ice[0]][ice[1]] -= 1
    return
        


N, M = map(int,input().split()) # 행과 열을 입력받음
sea = [list(map(int,input().split())) for _ in range(N)] # 바다 입력받음
year = 0 # 총 걸린 년수
cnt  = 0 # 빙하의 개수

while dfs(sea) <= 2:
    dmove(sea)
    eror = 0
    for i in range(N):
        for m in range(M):
            if sea[i][m] == 0:
                eror += 1
    if eror == N*M:
        break
print(year)