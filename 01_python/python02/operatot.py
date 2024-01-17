one = 3
two = 5
if one or two:
    print('or 연산 통과')
else:
    print('or 연산 통과 못함')

print(one or two)

three = ''
four  = 4

if three and four:
	print('3과 4')
else:
	print('실패')
      
print(three and four)


## 자주 쓰게 될 표현식

if one > 0 or one < 0:
	pass
if one !=0:
	pass
if one % 2 == 1:
	print('홀수')
else:
	print('짝수')
if one % 2:
	print('홀수')
	
print(one)