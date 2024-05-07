import sys
sys.stdin = open('input.txt')
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
  number = int(sys.stdin.readline())
  if number:
    heapq.heappush(heap, (abs(number), number))
  else:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  