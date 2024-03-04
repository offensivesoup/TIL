import sys
sys.stdin = open('input.txt')


w, h = map(int,input().split()) # 오른쪽 위, 왼쪽아래는 (0,0)으로 고정
p, q = map(int,input().split()) # 현재 개미 위치
t    = int(input())
cnt  = 0 # 움직인 횟수를 더해줄 것이다
row = (p+t) // w # 어디까지 갈건데 너
col = (q+t) // h

if row % 2 == 0:
    x = (p+t)%w
else:
    x = w - (p+t)%w

if col % 2 == 0:
    y = (q+t)%h
else:
    y = h - (q+t)%h
print(x,y)


