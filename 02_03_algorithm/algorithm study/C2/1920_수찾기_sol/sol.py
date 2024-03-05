import sys
sys.stdin = open('input.txt')

'''
안되는 in list는 in set으로 할 수 있으면 in set으로 해보자
'''

N = int(input())
background = set(map(int,input().split()))
M = int(input())
numbers = list(map(int,input().split()))
for number in numbers:
    if number in background:
        print(1)
    else:
        print(0)
