import sys
sys.stdin = open('input.txt')

'''
1. 끝나는 시간에 시작할 수 있는 회의들을 담는 것이 중요한데
일단 정렬?
'''

n = int(input())
meetings = [tuple(map(int,input().split())) for _ in range(n)]
meetings.sort(key=lambda x : (x[1], x[0]))
result = 0
print(meetings)
start = 0
for x, y in meetings:
  if x < start:
    continue
  start = y
  result += 1
print(result)