import sys
sys.stdin = open('input.txt')
 # A가 B를 먹음
T = int(input())
for test_case in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    B.sort()
    sumi = 0
    for a in A:
        start = 0
        end   = M-1
        result = 0
        while start <= end:
            mid = (start+end)//2
            if B[mid] >= a: # 만약 그 값이 a보다 큼
                end = mid - 1
            else:
                start = mid + 1
        sumi += start
    print(sumi)
