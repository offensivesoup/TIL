a, b = map(int,input().split())
mini = min(a, b)
resultMini = 0
while True:
    if a % mini == 0 and b % mini == 0:
        resultMini = mini
        break
    mini -= 1
print(mini)
print(a*b//mini)
