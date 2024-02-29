import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    stack = [0] * 1000
    top = 0 # 스택 만들기
    word = input()
    N    = len(word)
    stack[0] = word[0] # stack의 첫번쨰는 첫글자로 고정
    for i in range(1,N):
        if stack[top] != word[i]: # stack의 top이 입력값의 그 다음 글자와 다르면
            top += 1 # top을 1더해준다
            stack[top] = word[i] # 그 글자를 stack에 넣어준다.
        elif stack[top] == word[i]:
            stack[top] = 0
            top -= 1
    result = [x for x in stack if type(x) != int]
    print(f'#{test_case} {len(result)}')

