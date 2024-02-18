import sys
sys.stdin = open('input.txt')

N = int(input()) # 기둥의 개수
ground = [0] * 1001 # 기둥이 1000개니까 땅은 1001면적
build = [list(map(int,input().split())) for _ in range(N)]
maxi = 0
for b in build:
    if b[1] > maxi:
        maxi = b[1]
    ground[b[0]] = b[1]
result = 0
now = 0
for g in range(len(ground)):
    if ground[g] > now:
        now = ground[g]
        result += now
    elif now >= ground[g]:
        result += now
    if now != maxi:
            continue
    else:
        if maxi in ground[g+1:]:
            now = maxi
        else:
            break

ground.reverse()
now = 0
for g in range(len(ground)):
    if ground[g] > now:
        now = ground[g]
        if ground[g] == maxi:
            break
        result += now
    elif now >= ground[g]:
        result += now
    if now != maxi:
            continue
    else:
        break
print(result)