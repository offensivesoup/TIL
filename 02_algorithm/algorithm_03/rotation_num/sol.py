import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    result = []
    numLst90 = []
    numLst180 = []
    numLst270 = []
    # 90도 출력
    for i in range(N):
        num90 = ''
        for j in range(N-1,-1,-1):
            num90 += arr[j][i]
        numLst90.append(num90)
    result.append(numLst90)
    # 180도 출력
    for k in range(N-1,-1,-1):
        num180 = ''
        for l in range(N-1,-1,-1):
            num180 += arr[k][l]
        numLst180.append(num180)
    result.append(numLst180)
    # 270도 출력
    for m in range(N-1,-1,-1):
        num270 = ''
        for n in range(N):
            num270 += arr[n][m]
        numLst270.append(num270)
    result.append(numLst270)
    print(f'#{test_case}')
    for o in range(N):
        for p in range(len(result)):
            print(result[p][o], end = ' ')
        print()
    