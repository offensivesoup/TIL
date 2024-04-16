import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    n = int(input())
    officer = [list(map(int,input().split())) for _ in range(n)]
    officer.sort(key = lambda x : x[0])
    paperLst = [officer[0]]
    paperCnt = 1
    meetingCnt = 1
    for paper in range(1, n):
        if paperLst[-1][-1] >= officer[paper][-1]:
            paperLst.append(officer[paper])
            paperCnt += 1
        else:
            continue
    officer.sort(key = lambda x : x[1])
    meetingLst = [officer[0]]
    for meet in range(1,n):
        if meetingLst[-1][0] >= officer[meet][0]:
            meetingLst.append(officer[meet])
            meetingCnt += 1
        else:
            continue
    print(max(paperCnt, meetingCnt))