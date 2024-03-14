# 아래 함수를 수정하시오.
def count_character(char, cnt):
    return char.count(cnt)

def count_character(word, cnt):
    # 최종 결과물
    result = 0 # 해당하는 알파벳이 나올때마다 1씩 증가
    # 전체 순화
    for char in word:
        # print(text)
        # 순회해서 얻은 char 변수에서 얻은 값이
        # cnt 매개변수에 들어있는 값과 일치하다면
        if char == cnt:
            # result 에 담긴 값이 1씩 증가해야한다.
            # tmp = result + 1
            # result = tmp
            # 복합 연산자 += 을 사용
            result += 1
    # 전체 순회를 완료했다. -> 모든 상황에 대한 조사가 끝났다.
    return result

result = count_character("Hello, World!", "o")
print(result)  # 2




