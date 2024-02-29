import sys
sys.stdin = open('input.txt')


w, h = map(int,input().split()) # 오른쪽 위, 왼쪽아래는 (0,0)으로 고정
p, q = map(int,input().split()) # 현재 개미 위치
t    = int(input())
move = [(1,1),(1,-1),(-1,1),(-1,-1)]
cnt  = 0 # 움직인 횟수를 더해줄 것이다
## 경우의 수를 나눈다
m = 0
now = move[0]
while t > cnt:
    if p < w and q < h: # 둘다 작을때
        p += now[0]
        q += now[1]
        cnt += 1
        continue
    elif (p == w and q != h) # 오른쪽 벽에 닿임
        now = move[2] # 왼쪽 위로 가야지
        p += now[0]
        q += now[1]
        cnt += 1
        continue
    elif




