# 3 6 9 게임
# 3, 6, 9 == '-'로 표현한다
# 만약 36 이면 '--'로 표현한다(sep = '')
# 1부터 N까지 369를 진행한다.
## 2번, 3번, 치려면? -> 숫자를 문자열로 인식하여, 반복문 안에 넣고, 해당 문자열이 있으면 - 를 출력하는 형식
## 3과 6과 9가 숫자에 있다면(in) => -를 출력한다.
## 1000 미만의 수니까, 짝짝짝 까지만 구사하면 된다. 
## -> 조건문으로 묶어서, handLst 의 index로 사용될 hint 를 조건에 맞게 추가시키는 방향성 -> 예를 들어 hint 가 1이되면 짝짝, 0이면 두자리여도 하나만 있는 짝으로 구사된다.
## 숫자로 규칙성을 찾기 힘들기 때문에, user_input을 i의 문자형으로 사용
## i 가 10보다 작고, 3 6 9 면 그냥 짝
## i 가 2자리 숫자, 그럼 하나씩 탐색한다, 1 3 인 경우 한번만 있으므로, hint += 1이 한 번 작동, 그러고 인덱스에 넣으면 짝이 된다. 36은 2번 더해져서 짝짝이 리스트에 더해진다.
## 만약 둘다 없는 경우에는 그냥 숫자가 담길 수 있도록 else 를 준다.
## i가 3자리 숫자인 경우에도 마찬가지다.



N = int(input())
numLst = ['3', '6', '9']
handLst  = ['-', '--', '---']
userLst = []
# 문자열로 변환하여 넣어준다.
for i in range(1, N+1):
    hint = -1
    user_input = str(i)
    if i < 10 and user_input in numLst:
        userLst.append(handLst[0])
    elif 10 <= i < 100:
        for user in user_input:
            if user in numLst:
                hint += 1
        if hint > -1:
            userLst.append(handLst[hint])
        else:
            userLst.append(user_input)
    elif 100 <= i < 1000:
        for user in user_input:
            if user in numLst:
                hint += 1
        if hint > -1:
            userLst.append(handLst[hint])
        else:
            userLst.append(user_input)
    else:
        userLst.append(user_input)
        
for result in userLst:
    print(result, end = ' ')