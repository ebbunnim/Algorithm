import sys
sys.stdin = open("input.txt", "r")

def match(a):  # a, b는 "{", "}"처럼 짝으로 들어가는 str#이게 독립적으로 돌아서 짝을 매칭시키는게 에러
    stack = [0] * 10;
    top = -1; wrong=0

    for i in range(len(a)):
        if a[i] == "(":
            top += 1
            stack[top] = a[i]

        elif a[i] == ")" :
            if top == -1: #underflow 제어. 여기에 -1하면 underflow뜸
                wrong = 1
                break
            if stack[top] == "(":
                top -= 1

        if a[i] == "(" or a[i] == "{":
            top += 1
            stack[top] = a[i]

        elif a[i] == "}":
            if top == -1:
                wrong = 1
                break
            if stack[top] == "(":
                top -= 1

    if top == -1 and not wrong:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    a = input()
    if match(a): #{}없어도 안돌면 top=-1, wrong=0이므로 True
        print('#%d %d' % (tc, 1))
    else:
        print('#%d %d' % (tc, 0))


#
#
# import sys
# sys.stdin = open("input.txt", "r")
#
# def match(a):  # a, b는 "{", "}"처럼 짝으로 들어가는 str#이게 독립적으로 돌아서 짝을 매칭시키는게 에러
#     stack = [0] * len(a);
#     top = -1; wrong=0
#
#     for i in range(len(a)):
#         if a[i] == "(" or a[i] == "{":
#             top += 1
#             stack[top] = a[i]
#
#         if stack[top] == "(" :
#             if a[i] == ")":
#                 if top == -1: #underflow 제어. 여기에 -1하면 underflow뜸
#                     wrong = 1
#                     break
#                 stack[top] = 0
#                 top -= 1
#             elif a[i] == "}":
#                 wrong = 1
#                 break
#
#         elif stack[top] == "{":
#             if a[i] == "}":
#                 if top == -1:
#                     wrong = 1
#                     break
#                 stack[top] = 0
#                 top -= 1
#             elif a[i] == ")":
#                 wrong = 1
#                 break
#
#
#     if top == -1 and not wrong:
#         return True
#     return False
#
# T = int(input())
# for tc in range(1, T+1):
#     a = input()
#     if match(a): #{}없어도 안돌면 top=-1, wrong=0이므로 True
#         print('#%d %d' % (tc, 1))
#     else:
#         print('#%d %d' % (tc, 0))

