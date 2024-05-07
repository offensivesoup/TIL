import sys
sys.stdin = open('input.txt')



def find(parents, x):
  if parents[x] == x:
    return x
  parents[x] = find(parents, parents[x])
  return parents[x]

def union(parents, a, b):
  a = find(parents,a)
  b = find(parents,b)
  if a > b:
    parents[a] = b
  else:
    parents[b] = a

def connected(parents, cities):
  now = find(parents, cities[0])
  for city in cities[1:]:
    good = find(parents, city)
    if good != now:
        return "NO"
    good = now
    
  return "YES"  

n = int(input())
m = int(input())
area = [list(map(int,input().split())) for _ in range(n)]
cities = list(map(lambda x: int(x) - 1, input().split()))

parents = [i for i in range(n)]
for i in range(n):
  for j in range(n):
    if area[i][j] == 1:
      union(parents, i, j)
print(connected(parents, cities))      