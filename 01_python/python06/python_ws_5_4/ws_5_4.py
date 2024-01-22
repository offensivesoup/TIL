# 아래 함수를 수정하시오.
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
result = capitalize_words("hello, world!")
print(result)