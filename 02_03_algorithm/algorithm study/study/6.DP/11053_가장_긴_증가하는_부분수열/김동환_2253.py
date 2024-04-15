'''
1 2 3 4 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 100 2 101 3 102
1
(1 100) (1)
(1 100) (1 2)
(1 100 101) (1 2 101) (1 100) (1 2)
(1 100 101) (1 2 101) (1 2 3)
특정 숫자가 나왔을때
넣을 수 있으면 넣고, 넣었으면 원래꺼를 복사해놓음
아님 넘어가야함. => 완탐?
'''
import sys
sys.stdin = open('input.txt')
from collections import deque

def find_best(arr):
    global result
    while arr:
        now = arr.popleft()
        for i in range(len(find)):
            if find[i][-1] < now:
                find.append(find[i])
                find[i].append(now)

n = int(input())
arr = deque(list(map(int,input().split())))
find = [[arr[0]]]
result = 0
print(find)
find_best(arr)
print(find)