import sys
sys.stdin = open('input.txt')
from collections import Counter
sumi = 0
N = int(input())
numLst = [int(input()) for _ in range(N)]
# 산술평균
average = round(sum(numLst)/N)
# 중위수
mid = sorted(numLst)[N//2]
# 범위
length = len(range(min(numLst),max(numLst)))
# 최빈값
cnt = 0
c = Counter(numLst)
most = c.most_common()
maxi = most[0][1]
result = []
for num in most:
    if num[1] == maxi:
        result.append(num[0])
if len(result) >1:
    cnt = sorted(result)[1]
else:
    cnt = result[0]

print(average)
print(mid)
print(cnt)
print(length)
