import sys
sys.stdin = open('input.txt')
from pprint import pprint
'''
사다리게임으로 아이스크림 내기함
김대리가 사다리를 그리는데 문득궁금해짐
어느 사다리를 구하면 X로 갈 수 있을까?
'''

# for test_case in range(1,11):
#     T = int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]
#     for i in range(len(ladder)):
#         if ladder[99][i] == 2:
#             for j in range(len(ladder)-1,-1,-1):
#                 left_move = 0
#                 right_move = 0
#                 if i != 0 and ladder[j][i-1] == 1:
#                     for l in ladder[j][i:-1:-1]:
#                         if l == 0:
#                             break
#                         left_move += 1
#                 elif i != 99 and ladder[j][i+1] == 1:
#                     for r in ladder[j][i:]:
#                         if r == 0:
#                             break
#                         right_move += 1
#                 elif ladder[j][i] == 1:
#                     continue
#                 i += right_move
#                 i -= left_move
#                 select = i
#     print(f'#{test_case} {select}')

# for test_case in range(1,11):
#     T = int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]
#     endLst = []
#     for idx in range(len(ladder)):
#         if ladder[0][idx] == 1:
#             endLst.append(idx)
#     start_idx = ladder[99].index(2)
#     my_line   = endLst.index(start_idx)
#     for i in range(99,-1,-1):
#         if endLst[my_line] != 0 and ladder[i][endLst[my_line] - 1] == 1:
#             my_line -= 1
#         elif endLst[my_line] != 99 and ladder[i][endLst[my_line] + 1] == 1:
#             my_line += 1
#         else:
#             pass
#     print(f'#{test_case} {endLst[my_line]}')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    check = False
    result = 0
    ## 사다리의 크기 == 100 * 100
    for i in range(100):
        for j in range(100):
            # 출발 지점:
            if i == 0:
                if arr[0][0] == 1:
                    # 방문표시용 0으로 채워진 2차원 리스트
                    # visited = [[0] * 100] * 100
                    visited = [[0] * 100 for _ in range(100)]
                    # 출발 시점의 j 좌표 기록
                    original_j = j
                    while i != 99: # 탐색 시작 -> x가 99가 될 때 까지
                        # 내 지금 위치 방문 표시
                        # x, y = i, j # 이동
                        # 3방향 탐색 아래 왼쪽 오른쪽
                        for dir in [(1,0),(0,-1),(0,1)]:
                            # 현재위치 i, j 를 기준으로 dir[0], dir[1]
                            ni = i + dir[0] # 다음 탐색 대상 i좌표값
                            nj = j + dir[1] # 다음 탐색 대상 j좌표값
                            print(ni,nj, arr[ni][nj])
                            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1: # 이동 가능하다.
                                if not visited[ni][nj]:
                                    visited[i][j] = 1
                                    i, j = ni, nj # 이동
                            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 2:
                                result = original_j
                                check  = True
                                break
                        # 내가 한번이라도 2에 도착했다면
                        if check:
                            break
                    for visi in visited:
                        print(visi)
                # 내가 한번이라도 2에 도착했다면
                if check:
                    break
            # 내가 한번이라도 2에 도착했다면
            if check:
                break
    print(result)




