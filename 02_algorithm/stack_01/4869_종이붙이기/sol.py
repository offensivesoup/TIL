import sys
sys.stdin = open('input.txt')

'''
세로는 20으로 통일
10의 배수인 N
그럼 어차피 10부터 1
20은 3
30은 10에다 20을 가져다 붙이는 경우 + 1
1 3 5 11 21 43 85
'''

stack = [0] * 32
stack[1] = 1
stack[2] = 3
top = 2

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    num = N // 10
    while top <= num:
        top += 1
        stack[top] = (2*stack[top-2]) + stack[top-1]
    print(f'#{test_case} {stack[num]}')