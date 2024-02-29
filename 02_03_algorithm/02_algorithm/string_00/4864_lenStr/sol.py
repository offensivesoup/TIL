import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    total = 0
    for i in range(len(str2)-N+1):
        if str2[i:i+N] == str1:
            total += 1
        else:
            pass
    print(f'#{test_case} 1') if total >= 1 else print(f'#{test_case} 0')