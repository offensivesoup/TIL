import sys
sys.stdin = open('input.txt')

# 내코드

# d_row = [0,1]
# d_col = [1,0]
#
# def dfs(x, y, sumi):
#     global mini
#     if x == N-1 and y == N-1:
#         if sumi < mini:
#             mini = sumi
#             return
#     if sumi > mini:
#         return
#     for i in range(2):
#         dx, dy = x + d_row[i], y + d_col[i]
#         if 0 <= dx < N and 0 <= dy < N:
#             if not visited[dx][dy]:
#                 visited[dx][dy] = 1
#                 dfs(dx, dy, sumi+area[dx][dy])
#                 visited[dx][dy] = 0
#
# T = int(input())
# for test_case in range(1,T+1):
#     mini = 100000
#     N = int(input())
#     area = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     dfs(0,0,area[0][0])
#     print(f'#{test_case} {mini}')

# 강사님 코드

dx = [0,1]
dy = [1,0]

def search(x,y): # x,y 부터 조사 시작
    # 누적값인데 왜 data[x][y]의 값으로 초기화?
    stack = [[x, y, data[x][y]]] # 해당지점 도달까지 들었던 누적값
    while stack: # 모든 조사 대상 조사 완료할 때 까지
        x, y, cnt = stack.pop() # 이번 조사 대상 좌표와 누적값
        for k in range(2): # 우, 하 양방향 조사
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < N and ny < N: # 범위를 벗어나선 안된다.
                # 내가 [nx][ny] 번째에 도달하려고 할때 드는 누적값
                ## 이번 조사에서 쌓아온 누적값이, 누군가가 쌓아온 누적값 보다 적으면
                # 이동할 수 있어야 한다.
                if visited[nx][ny] > cnt + data[nx][ny]:
                    visited[nx][ny] = cnt + data[nx][ny]
                    stack.append((nx,ny,cnt + data[nx][ny]))


T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 방문 표시 리스트
    '''
        나중에는, 이곳에 특정 좌표에 도달하는데 드는 누적값을 기록
        그 누적값들은, 최솟값으로 갱신할 것이다.
        그럼 첫 비교 대상은 충분히 큰 값이어야 한다.
    '''
    visited = [[N*N*10] * N for _ in range(N)]
    search(0,0)
    print(f'#{test_case} {visited[N-1][N-1]}')
