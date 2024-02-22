import sys
sys.stdin = open('input.txt')

'''
태양이 삼촌의 커다란 참외밭 => 참외가 몇개나 있을까?
1제곱미터에 자라는 참외개수를 구하고, 넓이를 구하면 총개수를 구할 수 있었다!
개수는 이미 헤아렸음, 넓이만 구하면 됌
참외밭은 ㄱ-자 모양 혹은 ㄱ-자를 회전한 모양의 육각형이다.
돌면서 반시계 방향으로 지나는 변의 방향과 길이가 주어진다
참외수를 구하시오 -> 참외밭의 넓이를 구해라
동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
1. ㄱ 자면 3이 2개 1이 2개
2. ㄴ 자면 4랑 2가 2개
3. 거꾸로 ㄱ이면 4랑 1이 2개
4. 거꾸로 ㄴ이면 2랑 3이 2개
'''

K = int(input()) # 참외의 개수
area = [[0,0] for _ in range(5)] # 어차피 사각형에서 뺸거임
row = [] # 가로
col = [] # 세로
totalLst = []
for _ in range(6): # 변의 방향과 길이가 주어진다 참외밭 만들기
    direction , length = map(int,input().split())
    if direction == 1 or direction == 2:
        row.append(length)
        totalLst.append(length)
    else:
        col.append(length)
        totalLst.append(length)

a1 = max(row) * max(col)
maxr = totalLst.index(max(row))
maxc = totalLst.index(max(col))

m1 = abs(totalLst[maxr - 1] - totalLst[0 if maxr == 5 else maxr + 1])
m2 = abs(totalLst[maxc - 1] - totalLst[0 if maxc == 5 else maxc + 1])
print((a1 - (m1*m2)) * K)