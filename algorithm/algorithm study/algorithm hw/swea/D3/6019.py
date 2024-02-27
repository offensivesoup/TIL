T = int(input())

for test_case in range(1,T+1):
    D, A, B, F = map(int,input().split())
    T = (D*F)/(A+B)
    print(f'#{test_case} {T}')