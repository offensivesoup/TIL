import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 글자의 수
    user_input = input()
    num = [int(x) for x in user_input]
    one_cnt = 0
    max_v = 0
    idx = 0
    while idx < N:
        if num[idx] == 1:
            one_cnt += 1
        elif num[idx] == 0:
            one_cnt = 0
        if max_v < one_cnt:
            max_v = one_cnt
        idx += 1
    print(f'#{test_case} {max_v}')




