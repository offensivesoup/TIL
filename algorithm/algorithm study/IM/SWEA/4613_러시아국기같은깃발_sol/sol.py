import sys
sys.stdin = open('input.txt')

'''
깃발을 만들 수 있는 경우의 수
고로 최소값은, 모든 경우의 수를 비교해볼 수 있다.
그런데 각각 적어도 첫줄은 흰줄이고
마지막 줄은 빨간줄이다.
그럼 해당값을 먼저 고정시켜놓자.
고정 후 다음 순서로 진행시켜볼 수 있을 것같다
맨 바닥을 빨강, 맨 위를 하양 나머지 다 파랑 을 반복
4가지 경우의 수가 있는것이다
'''
def color(i, c):
    result = 0

    for j in range(M):
        if flags[i][j] != c:
            result += 1
    return result
def count(a,b):
    result = 0

    for i in range(0,N):
        if i < a:
            result += color(i,'W')
        elif a <= i < b:
            result += color(i,'B')
        else:
            result += color(i,'R')
    return result

def dfs(S,V):
    global answer
    if S == 2:
        result = count(res[0],res[1])
        if answer > result:
            answer = result
        return
    else:
        for i in range(V,len(nums)):
            res[S] = nums[i]
            dfs(S+1, i+1)

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    flags = [list(input()) for _ in range(N)]
    nums  = [i for i in range(N) if i]
    res = [None, None]
    answer = 1e9
    dfs(0,0)
    print(f'#{test_case} {answer}')