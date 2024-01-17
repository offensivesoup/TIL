# 미래를 보는 원재는 사재기를 한다고 한다.
# 감시가 심해서 한번에 많이는 할 수 없다 
# 1. 연속된 N일 동안의 물건의 매매가를 예측해서 알고 있다.
# 2. 당국의 감시망에 걸리지 않게 하루에 맥시멈 1 까지만 구입 가능
# 3. 파는건 얼마든지
# 1,2,3 이라면 3일에 팔면 3의 이득
## 최대 이익을 구하려면 ? 1일치 부터 N일치 까지의 탐색이 필요 -> for구문으로 구현
## 언제든 제일 비싼날 이전에 사서, 팔면 된다.
## 1. 제일 비싼날 구하고, 이전꺼 다 판다.
## 2. 해당 값들을 리스트에서 없애고 제일 비싼거 구해서 이전꺼 판다.
## 3. 반복해서 없으면 stop

T = int(input()) # 테스트케이스의 개수
buyLst = []
benefit = 0
for i in range(1, T+1):
    N = list(map(int(input().split()))) # 몇일을 예상할 수 있는지? == 몇일치 가격이 주어지는지
    sell_day = max(N)
    while True:
        if len(N) < 1:
            break
        maximum = N.index(sell_day) # 가장 최대값의 인덱스를 반환
        buying = [benefit + (sell_day - i) for i in N[:maximum]] # 첫 최대값 이전의 값을 반환해준다.
        buyLst.append(buying)

        



