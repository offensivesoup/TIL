# 아래 함수를 수정하시오.
def reverse_string(char):
    answer = ''.join(reversed(char)) # reversed가 호출한 결과가 reversed의 객체다.
    # 슬라이싱 => char[::-1]
    return answer

def reverse_string(word):
    # 최종 결과물 : 문자열
    # 왜? 하나씩 순회해서 하나씩 더해 나가야 하느냐?
    # 문자열은 immutable 하다. -> 원본 수정 안된다.
    result = ''
    # 순회를 뒤에서 부터 앞으로 반대순으로 해야함.
    # 그래서 대체적으로 sequence 순회시에는
    # range를 사용해서 index 기준 순회를 많이 사용한다.
    # range로 원래 word가 가진 각 요소를 출력
    for index in range(len(word)):
        # 문자열은 시퀀스니까, index접근 가능
        print(index, word[index])
    # len(word) -> 13
    # word가 13글자 : 12번 index까지만 있다.
    # range의 start 매개변수에 들어간 정수는
    # 해당 정수부터 범위를 설정한다.
    # 13번 index 부터 조회하면, word 길이를 초과한다.
    for index in range(len(word)-1, -1, -1):
        print(word[index])
        result += word[index]
    return result

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

