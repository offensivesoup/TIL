import sys
sys.stdin = open('input.txt')

T = int(input())

def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지)
    heap[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모 > 자식 비교를 위해
    p = c//2    # 부모번호 계산
    while p>=1 and heap[p] > heap[c]: # 부모가 있는데 더 크면 교환해
        heap[p], heap[c] = heap[c],heap[p] # 교환

for test_case in range(1, T+1):
    result = 0
    N = int(input())
    heap = [0] * (N+1)
    user_input = list(map(int,input().split()))
    last = 0
    for h in user_input:
        enq(h)
    while N > 0:
        N //= 2
        result += heap[N]
    print(f'#{test_case} {result}')
