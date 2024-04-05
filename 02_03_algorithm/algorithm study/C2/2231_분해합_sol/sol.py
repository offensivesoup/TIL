import sys
sys.stdin = open('input.txt')

'''
245 -> 245 + 2 + 4 + 5 = 256
216 -> 198 1 9 8
18
9
18
'''
num = int(input())
for i in range(1,num):
    string = list(str(i))
    plus = sum(map(int,string))
    if i + plus == num:
        print(i)
        break
else:
    print(0)


