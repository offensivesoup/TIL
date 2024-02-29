import sys
sys.stdin = open('input.txt')


w, h = map(int,input().split()) # 오른쪽 위, 왼쪽아래는 (0,0)으로 고정
p, q = map(int,input().split()) # 현재 개미 위치
t    = int(input())
cnt  = 0 # 움직인 횟수를 더해줄 것이다
## 경우의 수를 나눈다
m = 0
while t > cnt:
    if p <= w and q <= h:
        p += 1
        q += 1




