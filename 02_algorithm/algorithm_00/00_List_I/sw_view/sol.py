import sys
sys.stdin = open('input.txt')
'''
test_case = 100개
'''

for i in range(10):
    view = 0
    N = int(sys.stdin.readline())
    city = list(map(int,sys.stdin.readline().split()))
    for idx in range(2,N-2):
        # 총보아야할 빌딩이 5개야
        area = city[idx-2:idx+3]
        # 만약 조사 대상인 빌딩이 가장 높다면?
        if area.index(max(area)) == 2:
            T = max(area)
            area.remove(max(area)) # 해당 빌딩 뺴고
            view += T - max(area) # 그 다음 높은 빌딩만큼의 조망권 확보
        else:
            pass
    print(f'#{i} {view}')

# 강사님 코드

# 방법 1.

# for test_case in range(10):
#     result = 0
#     N = int(sys.stdin.readline())
#     data = list(map(int,sys.stdin.readline().split()))
#     # 각 건물의 최대 높이 255
#     for i in range(2, N-2):
#         min_value = 256
#         for j in range(5):
#             # 나와 나를 비교하는 상황은 무시
#             #if j == 2: continue
#             if j != 2:
#                 if data[i] - data[i-2+j] < min_value:
#                     min_value = data[i] - data[i-2+j]
#         # 조망권이 양수인 경우에만
#         if min_value > 0:
#             result += min_value
#     print(result)

# 방법 2.
for test_case in range(10):
    result = 0
    N = int(sys.stdin.readline())
    data = list(map(int,sys.stdin.readline().split()))
    for i in range(2,N-2):
        # 임시변수 I를 기준으로 5개 기준 선정
        max_neighbor = 0
        for j in range(i-2, i+3):
            # 나랑 나는 조사 안함
            if i == j : continue
            # j번째 위치가 조상대상 i번째보다 크면 무시
            if data[j] > data[i] and max_neighbor < data[j]:
                max_neighbor = data[j]
            elif data[j] >= data[i]:
                max_neighbor = data[i]
                break
            # 최종결과 = 나의 크기 - 내 이웃 중 젤 큰애
            # 조사 도중 취소된 경우
        result = data[i] - max_neighbor
            # # j번째 위치가 조사대상 i번째보다 작다면
            # if data[i] < data[i]:
            #     # 조사대상 크기 - j번째 아파트 크기
            #     temp = data[i] - data[j]
    print(result)