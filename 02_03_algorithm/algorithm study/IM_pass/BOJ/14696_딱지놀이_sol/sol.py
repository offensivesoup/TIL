import sys
sys.stdin = open('input.txt')

'''
두 어린이가 여러 장의 딱지를 가지고, 딱지놀이를 한다
딱지에는 별, 동그라미, 네모, 세모, 네가지 모양중 하나 이상의 모양이 표시
어느 것이 더 강력한 딱지인지
1. 두 딱지의 별의 개수가 같다면, 별이 많은 쪽이 이김
2. 별의 개수가 같고, 동그라미의 개수가 다르다면, 동그라미가 많은 딱지가 이김
3. 별, 동그라미가 같으면 네모가 많은
4. 별동그라미네모가 같으면 세모가 많은
5. 다 같으면 무승부
'''

N = int(input()) # 딱지 라운드 수
# 별, 동그라미, 네모, 세모 순 4 3 2 1
acnt, bcnt = 0, 0
for _ in range(N):
    aLst = list(map(int,input().split()))[1:]
    bLst = list(map(int, input().split()))[1:]
    result = 0
    for i in range(4,0,-1):
        if aLst.count(i) == bLst.count(i):
            continue
        else:
            if aLst.count(i) > bLst.count(i):
                result += 1
                break
            elif aLst.count(i) < bLst.count(i):
                result += 2
                break
    if not result:
        print('D')
    elif result == 1:
        print('A')
    else:
        print('B')
