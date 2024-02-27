import sys
sys.stdin = open('input.txt')

'''
난쟁이가 9명이 되었다 ㄷㄷ
키의 합이 100이 되어야 한다.
'''

hLst = [int(input()) for _ in range(9)]
subsets = [[]]
for i in hLst:
    L = len(subsets)
    for l in range(L):
        subsets.append(subsets[l] + [i])
        print(subsets)
for sub in subsets:
    if len(sub) == 7 and sum(sub) == 100:
        sub.sort()
        for i in range(7):
            print(sub[i])
        break