# 1. 최빈값을 구한다.
# 1-1. 3가지를 입력 받는다.(T, test_case, score)
# 1-2. count 를 통해 각 숫자를 인덱스로 취급할 수 있게, lst에 append 시킨다.
# 1-3. 최빈값에 대한 수치를 index로 확인할 수 있다.
# 2. 최빈값에 대한 중복 처리를 한다.
# 2-1. maximum 즉, 가장 빈도가 많은 값을 변수로 지정한다.
# 3. 값을 출력한다.

#### split(' ')은 공백을 따로 리스트에 추가하게 된다. swea에서 테스트케이스의 마지막 값이 공백이 되어있으면 map int 가 안된다. 즉, 공백을 기준으로 입력값을 구분하고자 하면 split()으로 주면 된다.

T = int(input())

for i in range(1,T+1):
    userLst = []
    maxLst  = []
    test_case = int(input())
    user_score = list(map(int,input().split()))
    for m in range(101):
    	userLst.append(user_score.count(m))
    maximum = max(userLst)
    for idx, score in enumerate(userLst):
        if maximum == score:
            maxLst.append(idx)
    if len(maxLst) == 1:
        result = maxLst[0]
        print(f'#{i} {result}')
    elif len(maxLst) > 1:
        result = maxLst[-1]
        print(f'#{i} {result}')