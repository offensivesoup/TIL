# import sys
# sys.stdin = open('input.txt')
earthLst = ["ZRO", "ONE" , "TWO", "THR", "FOR", "FIV","SIX", "SVN", "EGT", "NIN"]
T = int(input())
for test_case in range(1,T+1):
    strNumLst = []
    N, M = input().split()
    masLst = input().split()
    for i in range(int(M)):
        strNumLst.append(earthLst.index(masLst[i]))
    strNumLst.sort()
    print(N)
    for x in strNumLst:
        print(earthLst[x], end = ' ')
    print()