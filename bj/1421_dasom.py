# N, C, W = map(int,input().split())
# woods   = [int(input()) for _ in range(N)]
#
# profit = [] # 각 이득
# for i in range(1,max(woods)+1): # 젤 큰 나무까지 순회하면서 자연수 단위로 잘라봄
#     cart = [] # 자른거 담을 바구니
#     cut  = 0
#     total = 0
#     for wood in woods: # 나무 하나씩 꺼내서 잘라봄
#         cutting_wood = [i] * (wood // i)  # 잘라진 나무 더미
#         cart.append(cutting_wood) # 카트로 담아봄
#     for j in range(len(cart)):
#         if len(cart[j]) > 0: # 일단 최소 한덩이는 나왓음
#             if woods[j] % i == 0:
#                 cutting = len(cart[j]) - 1 # 이렇게 만들려고 몇번 잘랐니
#                 mymoney = sum(cart[j]) * W - (cutting * C) # 그럼 이 바구니 가격 나옴
#                 if mymoney > 0:
#                     total += mymoney
#             elif woods[j] % i != 0:
#                 cutting = len(cart[j])
#                 mymoney = sum(cart[j]) * W - (cutting * C) # 그럼 이 바구니 가격 나옴
#                 if mymoney > 0:
#                     total += mymoney
#     profit.append(total)
#
# print(max(profit))


N, C, W = map(int, input().split())
woods = [int(input()) for _ in range(N)]

moneys = []
for divisor in range(max(woods) + 1):
    if divisor == 0:
        wood_counts = []
        for wood in woods:
            wood_counts.append(woods.count(wood))
        for n in range(N):
            money = W * wood_counts[n] * woods[n]
    else:
        waste = 0
        count = 0
        for wood in woods:
            waste += wood % divisor
            if wood % divisor == 0:
                count += wood // divisor - 1
            else:
                count += wood // divisor
        money = W * (sum(woods) - waste) - (C * count)
        if money > 0:
            moneys.append(money)
        else:
            pass

print(f'{max(moneys)}')
