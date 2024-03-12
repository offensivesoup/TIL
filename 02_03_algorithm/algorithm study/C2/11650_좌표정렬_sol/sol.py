import sys
sys.stdin = open('input.txt')
N = int(input())
xy = [tuple(map(int,input().split())) for _ in range(N)]
xy.sort(key=lambda x:x[0]) # x 순으로 정렬
for result in sorted(xy):
    print(result[0], result[1])