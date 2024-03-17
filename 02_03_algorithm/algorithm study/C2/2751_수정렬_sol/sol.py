import sys
sys.stdin = open('input.txt')
N = int(input())
numbers = [int(input()) for _ in range(N)]

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right -1)
    quick_sort(arr, right+1, end)

quick_sort(numbers, 0, N-1)
for num in numbers:
    print(num)