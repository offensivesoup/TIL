my_dict = {}
my_dict['key'] = 3
print(my_dict)
numbers = []
## 배열은 고정된 id 값에 여러 요소들을 정리시키는 것
## 리스트에 값을 할당하려면
numbers += [1]
numbers.append(3)
numbers.extend([4,5,6])
numbers.insert(2,100)
print(numbers)

# 각 문자열을 모두 정수로 바꿔서 리스트에 담으시오
numbers_words = '1 2 3 4 5 6 7 8 9'

# 문자열을 순회하면서, 정수로 형변환이 가능하면...
# 정수로 형변환해서 리스트에 담는다.
# 최종 결과물

# 1번

numbers = []
for char in numbers_words:
    if char != ' ' and char.isnumeric():
        numbers.append(int(char))
print(numbers)

# 2번

numbers = [int(char) for char in numbers_words if char != ' ']
print(numbers)

# 3번

print(numbers_words.split())
numbers = list(map(int,numbers_words.split()))
print(numbers)

# 다른 상황

numbers_words = [
    '1 2 3 4 5',
    '6 7 8 9 10',
    '11 12 13 14 15'
]

## 최종 결과물
numbers = []
for word in numbers_words:
    conversion_list = list(map(int, word.split()))
    numbers.append(conversion_list)
print(numbers)

numberes = [list(map(int, word.split())) for word in numbers_words]
print(numberes)

numbers = [[0] * 10 for _ in range(10)] ## 아래와 위는 같다.
numbers = [[0 for _ in range(10)] for _ in range(10)]




