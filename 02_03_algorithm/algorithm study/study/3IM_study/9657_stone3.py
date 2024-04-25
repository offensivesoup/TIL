'''
1,3,4로 나누었을 때
홀수가 될 수 있으면 SK => 
아니면 CY
1 = SK 1
2 = CY 1 1
3 = SK 3
4 = SK 4
5 = SK 3 1 1
6 = SK 4 1 1
7 = CY 1 4 1 1
8 = SK
'''
# N = int(input())
# stone = [1,3,4]
# result = []
# for i in range(1,1001):
#     for s in stone:
#         if (i // s) % 2 == 1:
#            result.append(1)
#         else:
#             result.append(0)
# print(result) 
# m = 0
# while m < 3000:
#     print(result[m:m+3])
#     m += 3

# if answer[N-1] == 1:
#     print('SK')
# else:
#     print('CY')


# N = int(input())    
# arr = [0 for _ in range(1005)]
# arr[1] = 1
# arr[2] = 2
# arr[3] = 1
# arr[4] = 1
# for i in range(1, 1001):
#     num = 1

