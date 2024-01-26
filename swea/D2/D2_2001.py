# N*N의 숫자는 해당 영역 안에 존재하는 파리의 개수
# M*M의 크기의 파리채로 특정 영역을 선택했을때, 가장 max의 파리 수.
# 규칙성을 찾아보자
# 5*5 에서 만약 파리채가 1*1 이라면? 25번(5**2) 2*2라면16번(4**2) 3*3 9번 (3**2)
# 4*4라면 4번 2**2번 ...
# 6*6에서도 마찬가지일까? 1*1이라면 6**2 2*2라면 5**2 ...
## 어떤 사각형이든 파리채의 n - m + 1 의 제곱씩 움직인다.

T = int(input())

for i in range(1,T+1):
    area = [] # 사용자의 입력 영역
    paris = [] # 잡은 파리수 더해줄 영역
    N, M = map(int,input().split())
    # 사용자의 입력 영역 만들기
    for user_input in range(N):
        area.append(list(map(int,input().split())))
    for j in range(N):
        start_num = 0
        selected_area = area[j:j+M]
        if len(selected_area) == M:
            for _ in range(N-1):
                total = 0
                for row in selected_area:
                    pari_area = row[start_num:start_num+M]
                    for answer in pari_area:
                        total += answer
                start_num += 1
                paris.append(total)

    print(f'#{i} {max(paris)}')
                  

            

        # for j in range(N):
        #     num += selected_area[i][:j+M]
        #     num += area[]




