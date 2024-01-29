############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def tidy_up_company(email_list):
    result = {}
    for email in email_list:
        result[email] = 1 # 리스트를 순회한 딕셔너리를 만든다.
    for key in result: # 해당 딕셔너리의 키를 순회한다.
        emailCnt = 0
        for email in email_list: # 키 하나당, 리스트를 전부 순회한다.
            if key == email: # 해당 키와 이메일이 같으면
                emailCnt += 1 # 개수를 1 더한다.
                result[email] = emailCnt # 해당 값을 딕셔너리의 value로 저장한다.
    return result # 완성된 dict를 return 한다.
    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
