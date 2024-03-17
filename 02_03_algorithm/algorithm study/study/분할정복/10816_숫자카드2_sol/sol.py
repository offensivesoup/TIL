N = int(input())
sangen = list(map(int,input().split()))
M = int(input())
cards = list(map(int,input().split()))
result = {card:0 for card in cards}
for sang in sangen:
    if sang in result:
        result[sang] += 1
for card in cards:
    print(result[card], end = ' ')