import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    user_input = input() # 문자열 입력
    stack = [0] * len(user_input) # 문자열의 길이만큼 스택 만들기
    top = -1 # 탑
    result = 0 # 결과 담을 변수
    for word in user_input: # 문자열을 돕니다
        if word in "{(": # 문자열에 여는 괄호가 있으면
            top += 1 # push 합니다
            stack[top] = word
        elif word in "})": # 닫는괄혼데
            if stack: # 스택이 되어있으면
                if (stack[top] == '(' and word == ')') or (stack[top] == '{' and word == '}'): # 괄호의 쌍이 맞는다
                    stack[top] = 0 # 그러면 미리 들어가있던 괄호를 pop하고
                    top -= 1 # 앞으로 탑을 옮깁니다.
                else: # # 괄호의 쌍이 안맞으면
                    break # 나갑니다
            else: # 스택이 아니면
                break # 나갑니다
    else: #만약 닫는 괄호가 젤 먼저 나와서 포문이 못돌면 괄호만 넣고 나옵니다
        if stack[0] == 0: # 그렇게 스택의 처음이 0(다 순회하면)
            result = 1 # 1을 출력합니다
    print(f'#{test_case} {result}')
