arr = [324, 32, 22114, 16, 48, 93, 422, 21]

# 1. 정렬된 상태의 데이터가 필요
arr.sort()

# 2. 이진 검색 - 반복문 버전
def binarySearch(target):
    # 제일 왼쪽, 오른쪽 인덱스 구하기
    low = 0
    high = len(arr) - 1
    # 탐색횟수
    cnt = 0
    # 해당 숫자를 찾으면 종료
    # 더 이상 쪼갤 수 없을 때 까지
    while low <= high:
        mid = (low + high) // 2
        cnt += 1
        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binarySearch(21))

## 3. 이진 검색 재귀 함수 버전

def binarySearch(low, high, target):
    # 기저 조건 (언제까지 재귀가 반복되어야 할까)
    if low > high:
        return -1
    # 다음 재귀 들어가기 전에 무엇을 해야할까?
    mid = (low+high) // 2
    if arr[mid] == target:
        return mid
    # 다음 재귀 함수 호출 (파라미터)
    if target < arr[mid]:
        return binarySearch(low, mid-1, target)
    else:
        return binarySearch(mid + 1, high, target)
    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?

print(binarySearch(0,len(arr)-1,21))