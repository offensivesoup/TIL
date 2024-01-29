############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    area = []
    for i in range(N): # 사용자가 입력한 area를 만든다.
        for j in range(N):
            area.append((i,j))
    position = area.index(current) # 현 위치 의 인덱스 값을 반환
    if M == 0: # 위로 가려고 하는데
        if position + 1 > N: # 만약 현위치의 인덱스가, 가로값보다 크면 갈 수 있고(아래줄)
            return True
        else: # 아니면 못간다.
            return False
    if M == 1: # 아래로 가려고 하는데
        if position + 1 >= N * (N-1): # 현 위치가 맨 아래줄이면
            return False
        else:
            return True
    if M == 2: # 왼쪽으로 가려고하는데
        if position % N == 0: # 현위치가 맨 왼쪽이면
            return False # 못간다.
        else:
            return True # 간다.
    if M == 3: # 오른쪽으로 가려고 하는데
        if position == N-1: # 맨 오른 줄이면
            return False # 못간다.
        else:
            return True
    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
