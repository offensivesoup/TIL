# def f(pat,txt,M,N):
#     for i in range(N-M+1): # text에서 비교 시작 위치
#         for j in range(M):
#             if txt[i+j] != pat[j]: # 불일치면 다음 시작위치로
#                 break
#         else: # 패턴 매칭에 성공하면
#             return 1 # 1을 리턴한다.
#         # 모든위치에서 비교가 끝난 경우
#     return 0
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     pat = input()
#     txt = input()
#     M   = len(pat)
#     N   = len(txt)
#
#     ans = f(pat, txt, M, N)
#     print(f'#{tc} {ans}')
 
def kmp(t,p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0
    lps[0] = -1
    for i in range(1,M):
        lps[i] = j # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            print(i-M, end = ' ')
    print()
    return
















