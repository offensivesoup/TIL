# 아래 함수를 수정하시오.
# title 메서드가 하는 일:
# 공백을 기준으로 나뉜 알파벳의 첫 글자를 대문자로 변경
def capitalize_words(sentence):
    new_dict = {}
    new_lst = []
    for idx, char in enumerate(sentence):
        new_dict[idx] = char
    new_lst.append(new_dict[0].capitalize())
    for i in range(1, len(new_dict)):
        if new_dict[i-1] == ' ':
            new_lst.append(new_dict[i].capitalize())
        else:
            new_lst.append(new_dict[i])
    return ''.join(new_lst)


def capitalize_words(sentence):
    return sentence.title()

def capitalize_words(sentence):
    # 최종 결과물 : title화 된 문자열
    result = ''
    # word가 가진 요소 모두 순회
    # 조사 조건:
        # 첫 번째 글자거나, 글자가 공백 다음에 나타나면
        # 첫 번째 글자임을 알 수 있는 방법
        # index가 0이면 첫번째 글자임
        # index와 요소 자체 둘다 필요한 상황
    # enumerate와 range로 순회하는 차이는 무엇일까?..
    # range의 원목적 : 범위를 상정 -> 범위를 내가 자유롭게 작성가능
        # range로 범위 산정한 경우 : index만 나오므로
        # 요소만 보려면 word[index] 형식으로 작성해야한다.
    # enumerate의 목적 : 순회가능 요소의 각 요소와 index를 함께 반환
        # index는 index대로, 확인가능하고, 대상 요소 자체는 요소대로 사용 가능.
    for index in range(len(sentence)):
        print(sentence[index])
        # 내 위치는 index -> 내 앞번째 index -1
            # 단, 주의할 것, index가 0일때, index -1 을 조사하게 되면
            # 범위가 이상해질 수 있다.
            # 따라서 조건 잘 작성해야 한다.
        if index == 0 or temp == ' ':
            # word의 index번째 요소를 대문자로 바꿔서 result에 더하기
            result += sentence[index].upper()
        # 그 외 : 원본 그대로 일단 저장
        else:
            result += sentence[index]
        # 위에서 조사할때는 영향 안 미치도록
        # 각종 조사가 모두 끝나고 다음 순번 넘어가기 전에
        temp = sentence[index]
    return result



result = capitalize_words("hello, world!")
print(result)
