import sys
sys.stdin = open('input.txt')

isp = {'*' : 1, '+' : 0}
T = 10
for test_case in range(1,T+1):
    N = int(input())
    fx = input()
    stack = []
    # 후위표기법으로 바꾸기
    postfix = ''
    for tk in fx: # 식 순회
        if tk not in isp: # 만약 숫자라면
            postfix += tk
        elif tk in isp: # 기호라면
            if len(stack) < 1: # 스택이 텅 비어있으면
                stack.append(tk) # 일단 넣음
            else: # 아니면
                if isp[tk] >= isp[stack[-1]]: # 스택의 값보다 더 우선순위가 있거나 같으면
                    stack.append(tk) # 넣음
                else: #아니면
                    while stack: # 스택일 동안
                        if isp[stack[-1]] >= isp[tk]: # 지금 나온게 우선순위가 더 작거나 같을 때 까지
                            postfix += stack.pop() # 뺴볼거임
                        else:
                            break # 아니면 break
                    stack.append(tk) # 그걸 stack에 넣음
    # 계산하기
    for x in stack[::-1]: # 남은거, 마지막 숫자 나온 후에
        postfix += x # 거꾸로 해서 넣어줌
    num = [] # 계산 위한 스택 선언
    for tkk in postfix: # 후위표기법 식 순회
        if tkk.isdigit(): # 숫자면 넣음
            num.append(int(tkk))
        else: # 아니면
            A = num.pop() # 하나씩 빼서 계산
            B = num.pop()
            if tkk == '+':
                num.append(int(A)+int(B))
            elif tkk == '*':
                num.append(int(A)*int(B))
    print(f'#{test_case} {num[0]}') # 계산된 결과 나타냄