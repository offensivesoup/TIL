N, C, W = map(int,input().split())
woods   = [int(input()) for _ in range(N)]

# for i in range(max(woods)): # 나무가 100, 100, 100 이면 안짜르는게 이득 -> 최대 나무 길이로 잘라보자
#     porfit = 0 # 이득
#     cut_cnt = 0 # 몇번 잘랐니
#     for wood in woods: # 나무 하나씩 꺼내봄
#         if wood % i >= 1: # 나무가 잘랐는데 남았음
#             if wood % i > wood // (wood // i): # 남은 나무가 지금까지 조각난 나무보다 크고
#                 if (wood // i) * W > C: # 자르기 비용보다 이득임
#                     cut_cnt = (wood // i) + 1 # 그러면 잘라봄
#             else: # 아니면(남은나무가 지금까지 동강난거보다 작음)
#                 cut_cnt -= 1 # 어차피 버려야함
#             cut_cnt = (wood // i)
#         elif wood % i == 0: # 딱 맞게 잘랐음
#             cut_cnt = (wood // i) # 몇번 잘랐는지 나옴
    
profit = [] # 각 이득
for i in range(1,max(woods)+1): # 젤 큰 나무까지 순회하면서 자연수 단위로 잘라봄
    cart = [] # 자른거 담을 바구니
    cut  = 0
    total = 0
    for wood in woods: # 나무 하나씩 꺼내서 잘라봄
        cutting_wood = [i] * (wood // i)  # 잘라진 나무 더미
        cart.append(cutting_wood) # 카트로 담아봄
    for baguni in cart:
        if len(baguni) > 0: # 일단 최소 한덩이는 나왓음
            cutting = len(baguni) - 1 # 이렇게 만들려고 몇번 잘랐니
            mymoney = sum(baguni) * W - (cutting * C) # 그럼 이 바구니 가격 나옴
            total += mymoney
    profit.append(total)

print(max(profit))

        



