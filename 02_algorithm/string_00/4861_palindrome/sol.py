import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    word = [input() for _ in range(N)]
    area = []
    for w in range(N):
        var = []
        for v in range(N):
            var.append(word[w][v])
        area.append(var)
    for i in range(N):
        for j in range(N):
            hword = ''.join(area[j][i:i+M])
            if hword == hword[::-1] and len(hword) == M:
                print(f'#{test_case} {hword}')
    for k in range(N):
        for l in range(N):
            if k<l:
                area[k][l], area[l][k] = area[l][k], area[k][l]
    for p in range(N):
        for q in range(N):
            vword = ''.join(area[q][p:p+M])
            if vword == vword[::-1] and len(vword) == M:
                print(f'#{test_case} {vword}')
    