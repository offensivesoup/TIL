import sys
sys.stdin = open('input.txt')
'''
1 4 10 ...
1 3 6 10 15 ... 
1 2 3 4 5 6 7 ...
'''
apart = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
cnt = 1
if cnt < 14:
    for floor in range(1,15):
        for house in range(1,15):
            apart[floor].append(sum(apart[floor-1][:house]))
print(apart)
T = int(input())
for test in range(T):
    k = int(input()) # 층수
    n = int(input()) # 호수
    print(apart[k][n-1])
    