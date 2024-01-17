#호석이는 불면증이와서 양세기
#N의배수 번호인 양을 세기로 했다 즉 1,2,3,4 가 아닌 N, 2N, 3N ... kN 까지
#여기서 호석이의 궁금증은 1 2 4 8 16 이렇게 세었다면, 0부터 9까지를 다 세는 지점은 어디일까?

T = int(input()) # 테스트 케이스의 개수

for i in range(1,T+1):
    numberLst = []
    result = 0
    N = int(input()) # 몇부터 시작할 것인지
    while True: 
        N *= 2
        result += 1
        for m in str(N):
            numberLst.append(int(m))
        if len(set(numberLst)) == 10:
            break

    print(result)