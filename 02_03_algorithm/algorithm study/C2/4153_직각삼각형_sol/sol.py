import sys
sys.stdin = open('input.txt')

while True:
    tri = list(map(int,input().split()))
    tri.sort()
    if len(set(tri)) == 1 and list(set(tri))[0] == 0:
        break
    if tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2:
        print("right")
    else:
        print('wrong')
