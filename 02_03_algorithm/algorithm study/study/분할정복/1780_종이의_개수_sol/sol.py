import sys
sys.stdin = open('input.txt')

'''
N * N의 정사각형 종이가 있다.
각 칸에는 -1, 0, 1 중에 하나가 있다.
다음 규칙으로 이 종이를 자른다.
if 만약 종이가 모두 같은 수로 되어있다면:
    이 종이를 그대로 사용함
else:
    종이를 9개로 자른다. => 각각의 종이에 대해 위 과정을 반복
    -1 로만 채워진 종이, 0으로만 채워진 종이, 1로만 채워진 종이를 구해내야함

2630색종이 문제와 비슷하게 풀이하면 될 것같다.
가장 원초적으로 각 칸의 개수를 세어본다. 1*1 로 세었을 때 각 개수를
각 변수에 저장한다.
minus
zero
plus
다음, 3*3 크기에 대해 해당 과정을 반복하여, 만약 동일하다면
세어진 개수에 -8 개를 하는 것이 맞다.
'''

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)] # 첫 배열을 받아준다.
minus, zero, plus = 0, 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == -1:
            minus += 1
        elif arr[i][j] == 0:
            zero += 1
        else:
            plus += 1
row = 3
while row <= N:
    for m in range(0, N, row):
        for n in range(0, N, row):
            check = [] # 같은 숫자로 되어있는지 체크할 박스
            for p in range(row):
                for q in range(row):
                    check.append(arr[m+p][n+q])
            if len(set(check)) == 1: # 하나의 색으로 되어있으면
                if check[0] == -1:
                    minus -= 8
                elif check[0] == 0:
                    zero -= 8
                else:
                    plus -= 8
    row *= 3
print(minus)
print(zero)
print(plus)




