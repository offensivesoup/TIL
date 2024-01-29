############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len, sum 함수를 사용하지 않습니다.
def average_cost(cost_list):
    sumCost = 0  # 비용을 더할 sumCost 변수와
    sumCnt  = 0  # 더해진 개수를 알 sumCnt 변수를 선언한다.
    for cost in cost_list: # cost_list를 순회한다.
        sumCost += cost # cost를 누적합하여 sumCost에 할당한다. 
        sumCnt  += 1    # 더해진 횟수만큼(개수)sumCnt에 할당한다.
    result = sumCost / sumCnt
    return result

    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_cost([25, 40, 50, 55]))  # 42.5
print(average_cost([60, 70, 90, 80, 100, 35])) # 72.5
#####################################################
