import sys
sys.stdin = open('input.txt')

'''
자연수 A를 B번 곱한수를 알고 싶은데,
수가 너무 클 수 있으니까
이를 C로 나눈 나머지를 구해야해
A를 B번 곱하는 건 A의 B제곱이 되는데,
나머지가 나온다는 건, 일정한 패턴을 가진다는 것이다.
1부터 나누어보는 것이 시간초과가 난다.
그럼 일단 A % C 가 나머지가 있으려면
A%C가 0 이 아니어야 한다.
어차피 원래 나누어지는 거면, 뭘로 해도 나누어지기 떄문
'''

A, B, C = map(int,input().split())
start = 1
result = []
if A % C:
    while start <= B:
        answer = A**start%C
        if answer in result:
            break
        result.append(answer)
        start += 1
    print(answer)
else:
    print(0)