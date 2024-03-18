import sys
sys.stdin = open('input.txt')

## 퀵 정렬

def quick_sort(arr):
    ## 피봇값 보다 크면 오른쪽, 작으면 왼쪽에 옮긴다.
    if len(arr) < 2:
        return arr
    # 1. 피봇의 설정
    pivot = arr[0] # 첫째 값으로 골랐다.
    # 2. 배열을 돌아가면서, 교환한다.
    high = []
    low  = []
    for a in arr[1:]:
        if a > pivot:
            high.append(a)
        else:
            low.append(a)
    ## 피봇을 두 집합의 가운데에 위치시킨다.
    result = low + [pivot] + high
    ## 왼쪽 끝 / 오른쪽 끝 / 임의의 세 값 중에 중간 값
    return quick_sort(low) + [pivot] + quick_sort(high)
 

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(arr)
    print(quick_sort(arr))
    print(f'#{tc} {quick_sort(arr)[N//2]}')

