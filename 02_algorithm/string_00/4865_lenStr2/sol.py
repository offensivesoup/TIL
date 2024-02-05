import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    maxi = 0
    for w1 in str1:
        sumi = 0
        for w2 in str2:
            if w1 == w2:
                sumi += 1
        if maxi < sumi:
            maxi = sumi
    print(f'#{test_case} {maxi}')