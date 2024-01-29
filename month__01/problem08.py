############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list): 
    for idx in range(len(number_list)): # number_list의 개수만큼 순회한다.
        if number_list[idx] in number_list[idx+1:]: # 해당 numberlist의 요소가, 자신을 제외한 리스트에도 존재하면 pass
            pass
        else: # 자신과 같은 숫자가 없는 경우 (짝이 없는 경우)
             return number_list[idx] # 해당 숫자를 반환한다.
    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
