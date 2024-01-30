import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    cards = input()
    cnt = [0] * 10
    for card in cards:
        number = int(card)
        cnt[number] += 1
    print(cnt)
    result = 0
    for j in range(len(cnt)):
        if result <= cnt[j]:
            result = cnt[j]
            idx = j
    print(f'#{test_case} {idx} {result}')


