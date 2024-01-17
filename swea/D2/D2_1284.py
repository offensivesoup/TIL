# 종민이는 더 저렴한 수도 회사를 골라야 한다.
# 종민이가 사용하는 수도 양이 W 리터이다.
# A사는 1리터당 P의 값 즉 WP가 요금이 된다.
# B사는 R리터 이하면 Q만, R리터 초과이면 Q + WS 이다. 
# 결과는 종민이가 내야하는 수도요금이다. -> 1. 더 저렴한 회사를 고르고 2. 그 회사의 수도요금 측정

T = int(input())

for i in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    A_fee = W * P
    B_fee = Q
    if W > R:
        B_fee += (W-R) * S
    if A_fee > B_fee:
        print(f'#{i} {B_fee}')
    elif B_fee > A_fee:
        print(f'#{i} {A_fee}')