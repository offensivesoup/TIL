import random
# 1. 우리반 학생 전체 명단 리스트 만들기
students = ['김송희','최지우','강현성','장효승','이유찬','이창호','차민주','어지민','이승지','임경태','허유정','박동현','김구태','김종덕','박수빈','박재현','윤예리','정  훈','구현우','김동환','박지원','이승민','이권민', '      ']
# 2. 리스트를 무작위로 섞어주는 라이브러리 사용하기
random.shuffle(students)

# 3. 리스트를 순회해서 학생 이름 출력하기
# for student in students:
#     print(student)
# 4. 자리 모양에 맞춰서 출력하기
# 5. 출력 모양 꾸미기
print('==================== 스크린 ===================')
print('                                         김구현')
print()

for index in range(0, len(students), 6):  # range(n) -> 0 ~ n-1
    for i in range(6): # range(6) -> 0 ~ 6-1 
        if i != 0 and i % 3 == 0:
            print('     ', end=' ')
        print(students[index+i], end=' ')
    print() 



# ctrl + alt + 방향키 위, 아래 | 포커싱 증가
# ctrl + 왼쪽, 오른쪽 방향키
# alt + 방향키 | 포커싱 되어있는 줄 위치 이동
# alt + shift + 위 아래 방향키 | 포커싱 되어 있는 줄 복제