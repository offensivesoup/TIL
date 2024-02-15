import sys
sys.stdin = open('input.txt')

from collections import deque

# 피자가 빙글빙글 돈다
def rotation(f_pizza , w_pizza): # 피자(큐)와 오븐의 크기를 받는다
    while len(f_pizza) != 1:  # 오븐에 피자가 한판 남을때 까지
        c = f_pizza.popleft() # 입구쪽 피자 꺼내봄
        c[0] //= 2 # 그 치즈 반 녹아있음
        if c[0] != 0: # 그 피자의 치즈가 다 안녹음
            f_pizza.append(c) # 맨뒤로 놓음
        else: # 다 녹앗음
            if len(w_pizza) >= 1: # 남아있는 피자가 있으면
                next_pizza = w_pizza.popleft()  # 기다리는 피자중 젤 첫번째꺼 꺼내서
                f_pizza.appendleft(next_pizza)  # 첫피자로 넣어줌
            else: # 기다리는 피자는 없음
                continue # 그냥 오븐에서 계속 돌려봄
    return f_pizza[0][1] # 남은 피자번호 출력

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    user_input = list(map(int,input().split()))
    numLst = []
    for i in range(0,M):
        numLst.append([user_input[i],i+1])
    first  = deque(numLst[:N]) # 첫 오븐에 들어가는 피자
    wating = deque(numLst[N:]) # 기다리는 피자
    result_pizza = rotation(first, wating) # 피자 돌리기
    print(f'#{test_case} {result_pizza}') # 그 피자 번호 출력