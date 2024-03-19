import sys
sys.stdin = open('input.txt')

'''
N명의 직원이 N개의 일을 해야해
공평하게 분배할 거
직원 번호와 일 번호가 있고,
i번 직원이 j번 일을 하면, 성공 확률이 pi,j다
주어진 일이 모두 성공할 확률의 최댓값을 구해야한다.
'''

def backtracking(row, n, percent, visited):
    global maxi
    if row == n:
        if percent >= maxi:
            maxi = percent
    elif percent <= maxi:
        return
    for col in range(n):
        if not visited[col]:
            visited[col] = 1
            backtracking(row+1, n, officer[row][col] * percent, visited)
            visited[col] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    officer = [list(map(lambda x : float(x) / 100, input().split())) for _ in range(N)] # 직원들의 성공 확률
    visited = [0] * N
    maxi = 0
    backtracking(0, N , 1, visited)
    result = '{:.6f}'.format(round(maxi * 100, 6))
    print(f'#{tc} {result}')
