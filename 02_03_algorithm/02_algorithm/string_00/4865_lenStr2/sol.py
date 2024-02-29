import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1): # 테스트 케이스 순회
    str1 = input() # 각 문자 입력
    str2 = input()
    maxi = 0 # 최대값을 담을 변수
    for w1 in str1:
        sumi = 0 # 패턴을 순회하면서
        for w2 in str2:
            if w1 == w2: # 해당 글자와 원 문자의 글자가 동일하면
                sumi += 1 # sumi 변수 1 증가
        if maxi < sumi: # 만약 sumi 변수보다 maxi가 작으면
            maxi = sumi # maxi에 sumi 할당
    print(f'#{test_case} {maxi}')