import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
naming = [tuple(input().split()) for _ in range(N)]
print(naming)