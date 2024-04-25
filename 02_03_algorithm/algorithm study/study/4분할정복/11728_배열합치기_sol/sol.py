import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split()) # 배열 A의 크기, B의 크기
A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = A + B
result.sort()
print(*result)

