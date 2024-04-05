import sys
sys.stdin = open('input.txt')

'''
달팽이가 나무를 올라간다.
근데 달팽이는 어차피 딱 도착 전날만 알고, 거기서 +1 해준만큼 간다.
'''
A, B, V = map(int,input().split())
day = A - B # 하루에 이만큼 간다.
top = V - A # 여기까지 간다면 +1 해주면 된다.
## 근데 그게 딱맞으면 하루만 가고
## 근데 그게 더 가거나 덜가게 된다면
if top % day == 0:
    print(top // day + 1)
else:
    print(top // day + 2)

