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
        if area.index(max(area)) == 2:
            T = max(area)
            area.remove(max(area))
            view += T - max(area)
        else:
            pass
    print(f'#{i} {view}')

