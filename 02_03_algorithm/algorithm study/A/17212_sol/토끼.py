'''
1,2,5,7
'''

coin = int(input())

dp = [0] * 100001
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1

for i in range(8,100001):
    result = []
    if dp[i-7]:
        result.append(dp[i-7]+1)
    if dp[i-5]:
        result.append(dp[i-5]+1)
    if dp[i-2]:
        result.append(dp[i-2]+1)
    if dp[i-1]:
        result.append(dp[i-1]+1)
    dp[i] = min(result)
print(dp[coin])
         
    

