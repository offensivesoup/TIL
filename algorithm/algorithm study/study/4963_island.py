delta_row = [-1,1,0,0,-1,-1,1,1]
delta_col = [0,0,-1,1,-1,1,-1,1]

while True:
    w, h = map(int,input().split())
    visited = [[0] * w] * h
    result = 0
    island = []
    stack = []
    if w == 0 and h == 0:
        break
    area = [list(map(int,input().split())) for _ in range(h)]
    # 섬인 구역을 찾는다.
    for i in range(h): 
        for m in range(w):
            print(area[i][m])
            if area[i][m] == 1:
                if visited[i][m] != 1:
                    island.append([i,m]) # 1인 구역의 좌표들이 담겨져 있다.
                    if len(island) == 1:
                        break
    while island:
        # 섬 중 하나를 꺼내본다.
        point = island.pop()
        visited[point[0]][point[1]] = 1 # 그 섬은 간 것이다.
        for d in range(8): # 델타 탐색
            row = point[0] + delta_row[d]
            col = point[1] + delta_col[d]
            if row >= h - 1 or row < 0 or col >= w - 1 or col < 0:
                continue
            else:
                if area[row][col] == 1 and visited[row][col] != 1:
                    visited[row][col] = 1
                    island.append(point)
                    if point in island:
                        island.remove(point)
                else:
                    if len(island) >= 1:
                        island.pop()
                    elif len(island) == 0:
                        pass
        result += 1
                        
    print(result,'입니다')
                
    