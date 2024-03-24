import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    print(f'#{test_case}', end = ' ')
    N, N16 = input().split()
    for char in N16:
        print(format(int(char, 16), '04b'), end = '')
    print()