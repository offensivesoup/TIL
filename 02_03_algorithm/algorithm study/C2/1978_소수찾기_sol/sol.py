import sys
import math
sys.stdin = open('input.txt')

N = int(input())
numLst = list(map(int,input().split()))
result = 0
for i in range(N):
    if numLst[i] == 1:
        continue
    elif numLst[i] == 2 or numLst[i] == 3:
        result += 1
        continue
    for j in range(2, int(math.sqrt(numLst[i])+1)):
        if numLst[i] % j == 0:
            break
    else:
        result += 1
print(result)