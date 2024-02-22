# # 재귀함수
# def 어떤일을하는 함수:
#     if 이조건을 만족한다면:
#         return 특정값을 반환
#     elif 만족하지 못한다면:
#         어떤일을 하는 함수()
#
# while 이 조건을 만족하는 동안:
#     어떤 일을 수행
#
#
#
# 어떤일을하는 함수()

# def some(N):
#     if n == 0:
#         return 1
#     else:
#         n -= 1
#         print(n)
#         some(n)

def some():
    return 1

def other():
    return 1 + 2

result = some()
result2 = other()
print(result)
print(result2)