N = int(input())
boxes = list(map(int,input().split()))
arr = [0 for _ in range(N)]

j = N-1
while j != 1:
    for i in range(j):
        if boxes[j] > boxes[i]:
            arr[j] += 1
    j -= 1
print(arr)
