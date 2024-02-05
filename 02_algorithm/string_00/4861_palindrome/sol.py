import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    area = [input() for _ in range(N)]
    for i in range(N-M+1):
        for j in range(N):
            hword = ''.join(area[j][i:i+M])
            if hword == hword[::-1]:
                print(f'#{test_case} {hword}')
    for z in range(N):
        for k in range(N):
            vword = ''
            for l in range(N):
                if l+z > N:
                    break
                vword += area[l+z][k+z]
            if vword == vword[::-1] and len(vword) == M:
                print(f'#{test_case} {vword}')