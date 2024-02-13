import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    isp = {'*' : 4, '/' : 3, '+' : 2, '-' : 1, '.' : 0} # 연산당 번호 할당
    user_input = input().split() # 입력 받기
    stack = []
    for i in user_input: # 후위표기법 순회
        if i in isp: # 연산이라면
            if isp[i] == 0: # 종점이 나왔는데
                if len(stack) == 1:
                    print(f'#{test_case} {stack[0]}')
                else: # 연산자가 부족했던 경우
                    print(f'#{test_case} error')
                    break
            else:
                if len(stack) < 2:
                    print(f'#{test_case} error') # 연산자가 나왔는데 숫자가 미만인 경우
                    break
                else:
                    A = stack.pop()
                    B = stack.pop()
                    if isp[i] == 4: # 곱하기라면?
                        stack.append(A*B)
                    elif isp[i] == 3: # 나누기
                        if A == 0: # 0으로 나누려는 경우
                            print(f'#{test_case} error')
                            break
                        stack.append(B//A)
                    elif isp[i] == 2: # 더하기
                        stack.append(A+B)
                    elif isp[i] == 1: # 빼기
                        stack.append(B-A)
        else:
            stack.append(int(i))