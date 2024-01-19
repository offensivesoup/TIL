# 미래를 보는 원재는 사재기를 한다고 한다.
# 감시가 심해서 한번에 많이는 할 수 없다 
# 1. 연속된 N일 동안의 물건의 매매가를 예측해서 알고 있다.
# 2. 당국의 감시망에 걸리지 않게 하루에 맥시멈 1 까지만 구입 가능
# 3. 파는건 얼마든지
# 1,2,3 이라면 3일에 팔면 3의 이득
## 최대 이익을 구하려면 ? 1일치 부터 N일치 까지의 탐색이 필요 -> for구문으로
## [1,2,3,4,5,4,5] => max 5 그이전꺼 다 사서 팔면 됌, 해당 값들 없애고, 다시 맥스 반복
## 언제든 제일 비싼날 이전에 사서, 팔면 된다.
## 1. 제일 비싼날 구하고, 이전꺼 다 판다.
## 2. 해당 값들을 리스트에서 없애고 제일 비싼거 구해서 이전꺼 판다
## 3. 반복해서 없으면 stop
## ==> 시간이 너무 오래 걸림 (10개 중 7개 통과)
## While을 통한 접근이 아니라면?
## for 구문으로 N을 순차적으로 접근해 지울 필요가 없어진다면 작업 줄어들듯
## 거기에 필요한 논리
## 1. 총 N 회차의 반복이 필요
## 2. 거꾸로 간다면? 만약 앞에 값이 더 비싸면 뒤에값은 생각할 필요가 없어진다
## ex) 10 9 8 7 6 5 4 3 2 1 -> 1보다 2가 비싸니까 pass, 계속 pass => 0
## ex) 10 10 11 12 11 10 -> 10보다 11이 비싸니까 pass, 12 pass, 12보다 11이 싸네? 그럼 max = 12 그 담(이전) 값이 싸면 팔고, 비싸면 맥스 재설정



# 1번 시간초과 케이스

# T = int(input()) # 테스트케이스의 개수
# for i in range(1, T+1):
#     benefit = 0
#     buyLst = []
#     N = int(input()) # 몇일치 가격이 주어지는지
#     days = list(map(int,input().split())) # 몇일을 예상할 수 있는지? == 몇일치 가격이 주어지는지
#     while True:
#         benefitLst = []
#         if len(days) < 1:
#             break
#         sell_day = max(days)
#         maximum = days.index(sell_day) # 가장 최대값의 인덱스를 반환
#         for idx, data in enumerate(days[:maximum]):
#             benefitLst.append(sell_day - data)
#             days.remove(data)
#         for consume in benefitLst:
#             benefit += consume
#         days.remove(sell_day)
#     print(f'#{i} {benefit}')

# 2번 케이스

T = int(input())
for i in range(1,T+1):
    maxi, bene, Tmpi = 0, 0, 0
    N = int(input())
    days = list(map(int,input().split()))
    for m in range(N-1,-1,-1):
        if days[m] >= maxi:
            maxi    = days[m]
            bene   += Tmpi
            Tmpi    = 0
        else:
            Tmpi   += maxi - days[m]
            bene   += Tmpi
    print(bene)
            