import sys
sys.stdin = open('input.txt')

'''
자연수 A를 B번 곱한수를 알고 싶은데,
수가 너무 클 수 있으니까
그럼 먼가 곱셈의 법칙을 찾아야할거같다
2 의 4 승을 3으로 나눈 나머지를 알고 싶다면?
## 예시
100000 % 3 == 1
(10 ** 2) % 3 * (10 ** 2) % 3 * 10 % 3

10 ** 11 % 12
== ((10 ** 5) % 12 * (10 ** 5) % 12 * 10 % 12) % 12   
'''

A, B, C = map(int,input().split())
start = 1
result = []
