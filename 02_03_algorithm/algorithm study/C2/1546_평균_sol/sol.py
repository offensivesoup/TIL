import sys
sys.stdin = open('input.txt')

N = int(input())
scores = list(map(int,input().split()))
maxi = max(scores)
result = []
for score in scores:
    result.append(score/maxi*100)
print(sum(result)/N)