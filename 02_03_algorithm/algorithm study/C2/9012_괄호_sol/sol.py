import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    stack = []
    VPS = input()
    for v in VPS:
        if v == "(":
            stack.append("(")
        if v == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                    continue
            else:
                print("NO")
                break
            stack.append(")")
    else:
        if stack:
            print("NO")
        else:
            print("YES")


