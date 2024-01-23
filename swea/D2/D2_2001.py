# N*N의 숫자는 해당 영역 안에 존재하는 파리의 개수
# M*M의 크기의 파리채로 특정 영역을 선택했을때, 가장 max의 파리 수.

area = [] # 사용자의 입력 영역 (파리수)
paris = [] # 파리채 크기

T = int(input())

for i in range(1,T+1):
    N, M = map(int,input().split())
    # 사용자의 입력 영역 만들기
    for row in range(N):
        area.append(list(map(int,input().split())))
    

