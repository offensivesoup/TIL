# 주희가 부녀회장이 되고 싶어 각 층 사람을 모은 반상회 주최하려 함.
# 근데 이 아파트는 a층 b호에 사려면, a-1층의 1호부터 b호까지 사람들의 수의 합만큼
# 사람을 데려와 살아야함..
# 아파트에 빈집은 없고, 모두가 저 규칙을 지켯음
# 그럼 k층의 n호에는 몇명이사는지 구하는 프로그램
# 아파트는 0층부터 잇음, 1호부터 있음, 0층의 i호는 i명
# 첫째줄에 Test case 수, 첫줄에 k 둘째줄에 n이 주어짐
# k는 1이상, n은 14이하임
# 사용자는 1층이상의 14호이하의 집의 인원수를 알고자 하는 것임
# 그러면, 0층에는 각 호수에 맞는 인원이 살고 있음.
# 사용자가 1층에 1호에살려면, 0층의 1호인 1명 즉 1호는 전층다 1명임.
# 사용자가 1층의 2호에살려면, 1 + 2 즉 3명임
# 3호면, 1 + 2 + 3 즉 누적합 => 1층은 누적합의 층임.
# 사용자가 2층으로 간다면? 누적합의 누적합이 되는 거 아닌가?
# 2층의 3호면? 1층은 1 3 6 10명이되겠네
# 3층의 3호면? 1층은 1 3 6 2층은 1 4 10 3층은 1 5 16
# 다음 리스트를 구할 수 있었으면 좋겠다. => 1층은 0층의 누적합 리스트로 만들기
T = int(input())
zero_floor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(T):
    result = []
    answer = 0
    next   = []
    k = int(input())
    n = int(input())
    num = n*k
    for floor in range(k):
        next = []
        if floor == 0:
            zero_floor = zero_floor
        elif floor == 1:
            for i in range(len(zero_floor)):
                if i == 0:
                    next.append(zero_floor[i])
                else:
                    next.append(sum(zero_floor[:i+1])) # 1층의 카운트
        elif floor > 1:
            for i in range(len(zero_floor)):
                if i == 0:
                    next.append(zero_floor[i])
                else:
                    next.append(sum(zero_floor[:i+1])) # 2층 이상 카운트
        result.append(zero_floor)
    print(result)