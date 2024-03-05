# 소수는 그 수의 제곱근까지만 확인하면 된다이
N, M = map(int,input().split())
result = []
if M == 1:
    M = 2
for i in range(N,M+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5 + 1)):
        if i % j == 0:
            break
    else:
        print(i)
