import sys
sys.stdin = open('input.txt')

N = int(input())
people = [list(input().split()) for _ in range(N)]
people.sort(key = lambda x : int(x[0]))
for human in people:
    print(*human)