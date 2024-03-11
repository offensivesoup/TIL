K, N = map(int,input().split()) # 랜선의 개수, 필요한 랜선의 개수
lines = [int(input()) for _ in range(K)] # 랜선 받을 리스트
start = 1 # 젤 작은 값
end = max(lines) # 젤 큰 값
mid = (start + end) // 2  # 이진 탐색에 사용할 가운데 값
while start <= end: # 시작값이 끝값보다 작음
    cnt = 0
    for line in lines: # 줄을 하나씩 꺼내서
        cnt += line//mid # 자르고 나온 갯수 더해줄게
    if cnt >= N: # 그거 보단 조금 더 크게 잘라야 할 것 같아
        start = mid + 1
        mid = (start + end) // 2 # 탐색 범위를 바꾸어준다
    else: # 더 작게 잘라야 할 거 같어
        end = mid - 1 # 그럼 다시 잘라볼겡
        mid = (start + end) // 2
print(mid)