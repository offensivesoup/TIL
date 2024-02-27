import sys
sys.stdin = open('input.txt')

# 세로 가로 길이 10으로 고정

N = int(input())
matrix = [[0] * 100 for _ in range(100)]
for i in range(N):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] += 1
result = 10000

for m in range(100):
    for n in range(100):
        if not matrix[m][n]:
            result -= 1
print(result)


