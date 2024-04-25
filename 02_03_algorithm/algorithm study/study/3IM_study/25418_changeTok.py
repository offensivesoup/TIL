# i = 0
# while K != A:
#     if K % 2 == 0 and K // 2 >= A:
#         K //= 2
#         i += 1
#     else:
#         K -= 1
#         i += 1
#     if K <= A:
#         break
# print(i)

## 동환코드

A, K = map(int,input().split())

arr = [0 for _ in range(K+1)]
arr[-1] = 1
answer = 1
while arr[A] == 0:
    if K % 2 == 0 and K // 2 >= A:
        arr[K//2] = answer
        K //= 2
    else:
        arr[K-1] = answer
        K -= 1
    answer += 1
print(max(arr)) 



## 지우코드

A, K = map(int, input().split())

arr = [i for i in range(K+1)]

arr[A+1] = 1

if A*2 <= K:
    arr[A*2] = 1

if A+2 <= K:
    for i in range(A+2, K+1):
        if i%2 == 0:
            arr[i] = min(arr[i//2]+1, arr[i-1]+1, arr[i])
        else:
            arr[i] = min(arr[i-1]+1, arr[i])
        
    print(arr[K])
else:
    print(K-A)