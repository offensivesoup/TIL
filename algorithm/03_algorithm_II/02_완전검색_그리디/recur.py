# def kfc(x):
#     if x == 6:
#         return
#     print(x, end = ' ')
#     kfc(x+1)
#     print(x, end = ' ')
#
# kfc(0)
#
# # branch와 level 이해
#
# branch = 2
# level  = 3
#
# def kfc(x):
# 	if x == 3:
# 		return
#
#     for i in range(2):
#         kfc(x + 1)
#
# 순열
#
# path = []
#
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)
#
# # 중복 순열
#
# path = []
#
# def run(x):
#     if x == 3:
#         print(*path)
#         return
#
#     for i in range(1,7):
#         path.append(i)
#         run(x+1)
#         path.pop()
#
# run(0)
#
# path = []
# used = [False, False, False]
#
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         if used[i]: continue
#         used[i] = True
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#         used[i] = False
#
#
#
# N, T = map(int,input().split())
#
# path = []
# used = [False] * 7
#
# def Type1(x):
#
#     if x == N:
#         print(*path)
#         return
#
#     for i in range(1,7):
#         path.append(i)
#         Type1(x+1)
#         path.pop()
#
# def Type2(x):
#     if x == N:
#         print(*path)
#         return
#
#     for i in range(1,7):
#         if used[i]: continue
#         used[i] = True
#         path.append(i)
#         Type2(x+1)
#         path.pop()
#         used[i] = False
#
# if T == 1:
#     Type1(0)
# else:
#     Type2(0)

path = []
cnt = 0
def dice(x, sumi):
    global cnt
    if x == 3:
        if sumi == 10:
            cnt += 1
        return

    if sumi > 10:
        return

    for i in range(1,7):
        path.append(i)
        dice(x+ 1, sumi + i)
        path.pop()

dice(0, 0)
print(cnt)