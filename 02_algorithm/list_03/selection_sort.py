def selection_sort(a, N):
    for i in range(0,N-1): # 구간이 시작 i,2 개의 원소가 남을 때 까지
        min_idx = i        # 구간의 최소값 위치를 min_idx, 첫 원소를 최소로 가정
        for j in range(i + 1, N): # 실제 최솟값을 찾을 위치 j
            if a[min_idx] > a[j]:
                min_idx = j
        # 최솟값을 구간의 맨 앞으로 이동
        a[min_idx], a[i] = a[i], a[min_idx] # 최솟값을 국나의 맨 앞으로 이동

N = 5
arr = [-1,3,-2,5,2]
print(arr)
selection_sort(arr,N)
print(arr)

