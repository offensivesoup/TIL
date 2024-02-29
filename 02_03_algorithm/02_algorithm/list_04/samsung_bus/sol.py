import sys
sys.stdin = open('input.txt')
'''

'''
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    station = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    PLst = [int(input()) for _ in range(P)]
    print(f'#{test_case}', end = ' ')
    for s in PLst:
        stop = 0
        for stat in station:
            for k in range(stat[0],stat[1]+1):
                if k == s:
                    stop += 1
        print(stop, end = ' ')
    print()



