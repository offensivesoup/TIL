import sys
sys.stdin = open('input.txt')

def binary_search(arr, start, end, find, check):
    # 못찾았어
    if start > end:
        return False
    ## 중간값을 구해준다
    mid = (start + end) // 2
    ## 만약 arr의 그 중간값이 find(찾는 값)와 같다면 반환한다.
    if arr[mid] == find:
        return True
    ## 그 찾은 중간값이 찾는값보다 작아
    elif arr[mid] < find:
        ## 그러면 더 큰 값에서 찾는다.
        if check == 1:
            return False
        check = 1
        return binary_search(arr, mid + 1, end, find, check)
    ## 더 커
    else:
        if check == 2:
            return
        else:
            check = 2
        ## 더 작은 곳에서
        return binary_search(arr, start, mid - 1, find, check)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    cnt = 0
    for b in B:
        check = 0
        if binary_search(A, 0, N-1, b, check):
            cnt += 1
    print(f'#{tc} {cnt}')