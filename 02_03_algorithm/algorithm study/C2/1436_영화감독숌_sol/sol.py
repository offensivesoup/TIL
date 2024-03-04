numbers = []
for num in range(3000000):
    if '666' in str(num):
        numbers.append(num)
N = int(input())
print(numbers[N-1])