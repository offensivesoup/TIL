import sys
sys.stdin = open('input.txt')

'''
직사각형이 x,y p,q로 표현 근데 항상 pq가 오른쪽 위 꼭지점 xy 는 왼쪽 아래 꼭지점
두개의 직사각형이 등장하는 세가지 경우
1. 공통 부분이 직사각형인 경우 a로 출력
2. 공통 부분이 선분이 되거나, 점이 되는 경우 각각 b,c
3. 공통 부분 없이 완전히 분리되는 경우 d 출력
'''

for _ in range(4):
    user_input = list(map(int,input().split()))
    fs = user_input[:4] # 첫번째 사각형
    ss = user_input[4:] # 두번째 사각형
    fxy = (fs[0],fs[1])
    fpq = (fs[2],fs[3])
    sxy = (ss[0],ss[1])
    spq = (ss[2],ss[3])
    ## 경우의 수를 나눈다
    ## 공통부분이 직사각형인 경우 (첫번째 사각형이 두번째 안에 있거나, 두번째 사각형이 안에 있거나)
    if fxy[0] > sxy[0] and fxy[1] > sxy[1] and fpq[0] < spq[0] and fpq[1] < spq[1]: # 좌표가 사각형 안에
        print('d')
    elif sxy[0] > fxy[0] and sxy[1] > fxy[1] and spq[0] < fpq[0] and spq[1] < fpq[1]: # 좌표가 겹침
        print('d')