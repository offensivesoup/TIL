import sys
sys.stdin = open('input.txt')
sumi = 0
N = int(input())
numLst = [int(input()) for _ in range(N)]
average = sum(numLst)/N
# 산술평균
if abs(average - int(average)) >= 0.5:
    if average > 0:
        average = int(average) + 1
    else:
        average = int(average) - 1
else:
    average = int(average)
# 중위수
mid = sorted(numLst)[N//2]
# 범위
length = len(range(min(numLst),max(numLst)))
# 최빈값
cnt = 0
cntDict = {}
for num in numLst:
    cntDict[num] = numLst.count(num)
resultLst = []
for cnt in cntDict:
    if cntDict[cnt] == max(cntDict.values()):
        resultLst.append(cnt)
if len(resultLst) == 1:
    cnt = resultLst[0]
else:
    cnt = sorted(resultLst)[1]

print(average)
print(mid)
print(cnt)
print(length)
