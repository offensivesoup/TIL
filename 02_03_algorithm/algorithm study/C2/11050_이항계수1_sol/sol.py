import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

print(int(factorial(N)/(factorial(K)*factorial(N-K))))