import sys
sys.stdin = open('input.txt')

'''
정사각형들이 흰색 혹은 파란색 이걸 자를라고 함
while 모든 사각형이 색종이로 확정될때 까지:
    if 사각형의 색이 단일화 되어있지 않으면:
        가로와 세로로 중간을 잘라서 똑같은 4개의 색종이로 나눈다
    else: (같은 색이거나 더이상 자를수 없을때)
        if 그게 파란색임:
            파란색 색종이 더해줌
        else: (그게 흰색임):
            흰색 색종이 더해줌 
조건:
1. N은 2의 7승까지임
2. 흰색은 0 파란색은 1로 표현한다.
3. 첫째 즐에 흰색 색종이, 둘째 줄에 파란 색종이 출력

걍 어차피 완탐하면 시간 복잡도가 너무 크게 나타난다( 직접 자르는 로직을 구현 )
아니 그럼 쉽게 생각하면
일단 1,1로 다 잘라볼거임 그럼 흰색 파랑이 몇개네?
다음 2,2로 잘라볼거임 어? 만들어 지네
다시 가져다 붙여야지 => 1로 센거에서 3을 빼야지(3개 더해서 하나로 세어버렸으니까)
다음 4,4로 세야지 어? 되네 => 4로 센거에서 2의 제곱을 빼준다. 
8, 8로 세었는데 세지네? => 8의 제곱에서 4의 제곱을 빼준다.
이렇게 해서 어차피 128까지 밖에 안감
16 32 64 128 까지만 해주면댐
'''

N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
blue = 0
white = 0
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            blue += 1
        else:
            white += 1
size = 2
while size <= N:
    for i in range(0,N-size+1,size):
        for j in range(0,N-size+1,size):
            check = []
            for p in range(i,i+size):
                for q in range(j,j+size):
                    check.append(area[p][q])
            if len(set(check)) == 1: # 그게 색종이가 되네?
                if check[0] == 0: # 그게 흰색이네?
                    white -= 3 # 그 전 색종이의 크기를 뺸만큼 더 쓴거니까, 이걸 뺴주어야함
                else: # 그게 파랑이네?
                    blue -= 3
    size *= 2 # 사이즈를 키워봄
print(white)
print(blue)

