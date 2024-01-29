############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def check_user_id(user):
    userId = user['user_id'] # user_id의 value값을 할당한다.
    result = 0
    for _ in userId: # userId를 순회한다.
        result += 1  # 순회한 횟수만큼 result에 누적합한다.
    
    if result >= 4 and result < 16: # result가 4이상 16미만이면
        return True # True 반환
    else:
        return False # 아니면 False를 반환한다.
    

    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(check_user_id(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_user_id(user_data2))  # False
#####################################################
