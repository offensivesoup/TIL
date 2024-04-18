import sys
sys.stdin = open('input.txt')

n = int(input())
drinks = list(map(int,input().split()))
result = 0
result += drinks.pop(drinks.index(max(drinks)))
result += sum(drinks) / 2
if result - int(result) > 0:
    print(result)
else:
    print(int(result))
