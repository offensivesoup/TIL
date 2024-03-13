import sys
sys.stdin = open('input.txt')

N = int(input())
sangen = list(map(int,input().split()))
M = int(input())
cards = list(map(int,input().split()))
result = [0] * M
for i in range(M):
    result[i] = sangen.count(cards[i])
print(*result)