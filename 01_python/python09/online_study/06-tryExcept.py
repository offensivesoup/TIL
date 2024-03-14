# try:
#     print(name)
# except Exception as ex:
#     print(ex)

# try:
#     num = int(input('숫자 입력'))
# except ValueError:
#     print('숫자가 아닙니다.')


## 복수 예외 처리 연습
    
## 100으로 나눌 값을 사용자에게 입력해달라고 하면 -> valueError, zerodivisonError
    
# try:
#     num = int(input('100으로 나눌 숫자를 입력하시오.'))
#     print(100 / 0)
# except BaseException:
#     print('숫자를 넣어줘')
# except ZeroDivisionError:
#     print('0으로 나누기가 될 것 같아?')
# except:
#     print('알수없는 에러가 발생했음')

# 딕셔너리에서 키를 조회할 때
# 키가 없다는 상황

my_dict = {}

# try-except

try:
    result = my_dict['a']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# if -else

if 'a' in my_dict:
    result = my_dict['a']
    print(result)
else:
    print('Key가 존재하지 않습니다.')





