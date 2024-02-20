import sys
sys.stdin = open('input.txt')

def pre_order(T):
    if T:
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input()) # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int,input().split()))
left = [0] * (N+1) # 부모를 인덱스로 왼쪽자식번호 저장
right = [0] * (N+1) # 오른쪽 자식
par  = [0] * (N+1)  # 자식을 인덱스로 부모 저장
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in arr[i], arr[i+1]:
#     p, c = arr[i], arr[i+1] 이렇게도 할 수 있다.
    if left[p] == 0: #왼쪽자식 이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0: # 부모가 있으면
    c = par[c] # 부모를 새로운 자식으로 해서
root = c  # 더 이상 부모가 없으면 root
print(root)

c = N
while par[c] != 0:
    c = par[c]
root = c
pre_order(root)
# print(root)
