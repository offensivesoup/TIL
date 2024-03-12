import sys
sys.stdin = open('input.txt')

K, N = map(int,input().split()) # 막걸리의 수, 사람 수
sangtak = [int(input()) for _ in range(K)] # 막걸리들
start = 1 # 젤 작은 값
end = max(sangtak) # 젤 큰 값
mid = (start + end) // 2  # 이진 탐색에 사용할 가운데 값
while start <= end: # 시작값이 끝값보다 작음
    cup = 0
    for sang in sangtak: # 막걸리 꺼내서
        cup += sang//mid # 컵에 담아줄게
    if cup >= N: # 그거 보단 조금 더 많이 담아할거 같애
        start = mid + 1
        mid = (start + end) // 2 # 탐색 범위를 바꾸어준다
    else: # 더 적게 따라야할 거같애
        end = mid - 1 # 그럼 다시 부어볼게
        mid = (start + end) // 2
print(mid)