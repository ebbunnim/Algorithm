import sys
sys.stdin = open("input.txt", "r")

def match(a):  # a, b는 "{", "}"처럼 짝으로 들어가는 str#이게 독립적으로 돌아서 짝을 매칭시키는게 에러
    stack = [0] * len(a);
    top = -1;

    for i in range(len(a)):
        #열린 괄호때는 얘만 돌음
        if a[i] == "(" or a[i] == "{":
            top += 1
            stack[top] = a[i]

        if a[i] == ")":
            if stack[top] == "{":
                return False
            if stack[top] == "(":
                if top == -1:
                    return False
                stack[top] = 0
                top -= 1
        if a[i] == "}":
            if stack[top] == "(":
                return False
            if stack[top] == "{":
                if top == -1:
                    return False
                stack[top] = 0
                top -= 1

    if top == -1:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    a = input()
    if match(a): #{}없어도 안돌면 top=-1, wrong=0이므로 True
        print('#%d %d' % (tc, 1))
    else:
        print('#%d %d' % (tc, 0))

