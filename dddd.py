import sys
sys.stdin = open('input.txt')

'''
0~9까지의 숫자카드에 6장을 뽑아서 나열
3장의 카드가 연속적인 숫자면 run
3장의 카드가 동일한 번호면 triplet
run과 triple로만 구성되어있으면
baby-gin이다. 
'''

def baby_gin(num):
    run    = 0
    triplet = 0
    N = 6
    cntLst = [0] * 10
    # triplet인지 먼저 확인
    # 3장 이상의 카드가 동일한 카드라면 triplet
    # trip_cnt로 각 숫자별 개수를 세서, 해당 리스트의 3의 개수를 세어본다.
    for i in str(num):
        cntLst[int(i)] += 1
    for j in range(len(cntLst)):
        if cntLst[j] >= 3:
            triplet += 1
            cntLst[j] -= 3
    for k in range(len(run_cnt)):
        if 0 not in run_cnt[k:k+3]:
            run += 1
    
    if run + triplet >= 2:
        return True
    else:
        return False
    
T = int(input())
for test_case in range(1,T+1):
    user_num = int(input())
    print(f'#{test_case} {baby_gin(user_num)}')
        