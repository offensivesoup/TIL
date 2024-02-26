import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    num  = list(map(int,input().split()))
    student = list(range(1,N+1))
    for n in num:
        student.remove(n)
    student.sort()
    print(f'#{test_case}', end = ' ')
    print(*student)