import sys
sys.stdin = open('input.txt')

'''
'''

n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)

x_triangle, y_triangle = 0, 0
for i in range(n-1):
    x_triangle += x[i] * y[i+1]
    y_triangle += y[i] * x[i+1]
x_triangle += x[-1] * y[0]
y_triangle += y[-1] * x[0]
print(round(abs((x_triangle - y_triangle)/2),1))