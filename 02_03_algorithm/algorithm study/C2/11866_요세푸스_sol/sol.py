import sys
sys.stdin = open('input.txt')
from collections import deque

N, K = map(int,input().split())
circle = list(range(1,N+1))
result = []
point  = 0 
while circle:
    point += K - 1
    if point >= len(circle):
        point %= len(circle)
    result.append(str(circle.pop(point)))

print("<", ", ".join(result), ">", sep = "")