import sys
sys.stdin = open('input.txt')

from collections import deque

while True:
    try:
        T = int(input())
        password = deque(map(int, input().split())) # 암호 입력받기
        i = 1
        while True:
            c = password.popleft()  # 맨 왼쪽꺼 뺀다
            c -= i  # 자리수만큼 뺀다
            if c <= 0:
                c = 0
                password.append(c)
                break
            password.append(c)
            if i < 5:
                i += 1
            else:
                i = 1
        print(f'#{T}',*password)
    except:
        break