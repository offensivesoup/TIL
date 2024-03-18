import sys
sys.stdin = open('input.txt')

T = int(input())

def merge_sort(user_arr):
    global cnt
    if len(user_arr) < 2: return user_arr
    mid = len(user_arr)//2
    left = merge_sort(user_arr[:mid])
    right = merge_sort(user_arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    if left[-1] > right[-1]:
        cnt += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr

for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')