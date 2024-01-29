############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    # start 지점을 반환해야함
    for arr in matrix:
        if 1 in arr:
            result = [matrix.index(arr),arr.index(1)]
        else:
            pass
    v = result[0]
    h = result[1]
    for move in move_list:
        if move == 0:
            if 1 in matrix[0]:
                return None
            else:
                v -= 1
        if move == 1:
            if 1 in matrix[-1]:
                return None
            else:
                v += 1
        if move == 2:
            if h == 0:
                return None
            else:
                h -= 1
        if move == 3:
            if h == N - 1:
                return None
            else:
                h += 1
    return [v,h]
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
