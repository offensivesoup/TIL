N = int(input())
number = 1
for i in range(2,N+1):
    number *= i
result = 0
for s in str(number)[::-1]:
    if s == '0':
        result += 1
    else:
        break
print(result)