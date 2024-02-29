T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    cnt = 0
    aline = []
    bline = []
    for _ in range(N):
        ai, bi = map(int,input().split())
        aline.append(ai)
        bline.append(bi)
    for i in range(N):
        for j in range(N):
            if i != j:
                if aline[i] > aline[j] and bline[i] < bline[j]:
                    cnt +=1
    print(f'#{test_case} {cnt}')