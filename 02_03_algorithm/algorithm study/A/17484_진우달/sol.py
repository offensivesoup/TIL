import sys
sys.stdin = open('input.txt')

'''
백트래킹?

'''

def travel(now, sumi, arrive, back):
    # 도착하면 종료
    global mini
    if arrive == N-1:
        if mini > sumi + space[arrive][now]:
            mini = sumi + space[arrive][now]
            return
        return
    if mini < sumi:
        return
    if back == 'start':
        if now == 0:
            travel(now, sumi+space[arrive][now], arrive+1,0)
            travel(now+1, sumi+space[arrive][now], arrive+1,1)
        elif now == M-1:
            travel(now, sumi+space[arrive][now], arrive+1,0)
            travel(now-1, sumi+space[arrive][now], arrive+1,-1)
        else:
            travel(now+1, sumi+space[arrive][now], arrive+1,1)
            travel(now, sumi+space[arrive][now], arrive+1,0)
            travel(now-1, sumi+space[arrive][now], arrive+1,-1)
    else:
        if now == 0:
            if back == -1:
                travel(now, sumi+space[arrive][now], arrive+1,0)
                travel(now+1, sumi+space[arrive][now], arrive+1,1)
            elif back == 0:
                travel(now+1, sumi+space[arrive][now], arrive+1,1)
        elif now == M-1:
            if back == 1:
                travel(now, sumi+space[arrive][now], arrive+1,0)
                travel(now-1, sumi+space[arrive][now], arrive+1,-1)
            elif back == 0:
                travel(now-1, sumi+space[arrive][now], arrive+1,-1)
        else:
            if back == -1:
                travel(now+1, sumi+space[arrive][now], arrive+1,1)
                travel(now, sumi+space[arrive][now], arrive+1,0)
            elif back == 0:
                travel(now+1, sumi+space[arrive][now], arrive+1,1)
                travel(now-1, sumi+space[arrive][now], arrive+1,-1)
            else:
                travel(now, sumi+space[arrive][now], arrive+1,0)
                travel(now-1, sumi+space[arrive][now], arrive+1,-1)


N, M = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(N)]
mini = 1e9
for i in range(M):
    travel(i, 0, 0, 'start')
print(mini)