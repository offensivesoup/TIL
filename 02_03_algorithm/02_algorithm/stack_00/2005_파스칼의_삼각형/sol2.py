import sys
sys.stdin = open('input.txt')

## 강사님 코드

# memo = [[1] * 10 for _ in range(10)]
#
# for i in range(1,10):
#     for j in range(1,10):
#         if i != j:
#             memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
#
# T = int(input())
#
# for test_case in range(1,T+1):
#     N = int(input())
#     print(f'#{test_case}')
#     for i in range(N):
#         print(*memo[i][:i+1])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = [[1] for i in range(N+1)]
    a[1] = [1]
    a[2] = [1,1]
    print(a)

    for n in range(3,N+1):
        for m in range(len(a[n-1])-1):
            a[n].append(a[n-1][m]+a[n-1][m+1])
        a[n].append(1)
    print(f'#{tc}')
    for i in a[1:]:
        print(*i)