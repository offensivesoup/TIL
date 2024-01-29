############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):
    userPw = user['password'] # 각각의 값을 할당한다.
    pwConfirm = user['password_confirm']
    lengthPw = 0
    for _ in userPw:
        lengthPw += 1
    if lengthPw >= 8 and lengthPw < 32: # 비밀번호의 개수가 8자 이상, 32자 미만
        if userPw == pwConfirm: # 개수를 충족하고 confirm을 확인하여
            return True # 두 조건을 모두 충족하면 True
        else:
            return False # 개수만 충족하면 False
    else:
        return False # 개수부터 충족하지 못하면 False
    
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
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################