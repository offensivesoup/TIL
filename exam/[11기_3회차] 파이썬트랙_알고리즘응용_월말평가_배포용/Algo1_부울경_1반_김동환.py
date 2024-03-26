T = int(input())

for test_case in range(1, T+1):
    result = 0 # 결과를 담을 변수
    category, num = input().split() # 몇진법인지, 어떤 숫자인지 입력을 받는다
    if category == '24': # 2진수로 표현되어있다면
        result = format(int(num,2),'06x').upper() # 6자리 16진수 대문자로 표현해준다
    elif category == '6': # 16진수로 표현되어있다면
        result = format(int(num,16),'024b') # 0을 생략하지 않은 24자리 2진수로 표현해준다.
    print(f'#{test_case} {result}')