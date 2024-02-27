# ## 재귀함수 스택
#
# def f2(n):
#     n *= 2
#     print(n)
#
# def f1(c,d):
#     e = c+d
#     f2(e)
#
# a = 10
# b = 20
# c = a + b
# f1(a,b)
#
# ## 피보나치 수열
#
# def fibo(n):
#     if n<2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(8))
#

def f(i,k):    # 현재위치 i, 목표치 k
    if i == k:
        print(brr)
    else:
        brr[i] = arr[i]
        f(i+1,k)


arr = [10,20,30]
N   = len(arr)
brr = [0] * N
f(0, N)
