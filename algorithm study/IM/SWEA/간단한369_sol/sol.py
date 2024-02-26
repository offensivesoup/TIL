import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1,N+1):
    handsclap = ''
    if '3' not in str(i) and '6' not in str(i) and '9' not in str(i):
        print(i, end = ' ')
    else:
        for s in str(i):
            if s == '3' or s == '6' or s == '9':
                handsclap += '-'
        print(handsclap, end = ' ')
