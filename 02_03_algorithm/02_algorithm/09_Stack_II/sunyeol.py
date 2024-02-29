def f(i,k,s):
    global cnt
    global min_v
    cnt += 1
    if i == k:
        # print(*P)
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):  # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i] # P[i] <-> P[j]
            f(i+1, k, s + arr[i][P[i]])
            P[i], P[j] = P[j], P[i] # 원상
            # 복구

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, N, 0)
print(min_v, cnt)