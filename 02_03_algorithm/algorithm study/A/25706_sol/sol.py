import sys
sys.stdin = open('input.txt')

n = int(input())
field = list(map(int,input().split()))
dp = [1] * (n)
for i in range(n-2,-1,-1):
    if not field[i]:
        dp[i] = dp[i+1] + 1 
    else: # 점프대가 있으면
        if i + field[i] > n - 2: # 그 점프대를 밟아서 끝까지 넘어갔다면
            dp[i] = 1 # 거기밟으면 끝남
        else: # 밟고 더 갈게 있으면
            dp[i] = dp[i+field[i]+1] + 1 # 그 점프대의 높이만큼 넘어가면된다.


print(*dp)
