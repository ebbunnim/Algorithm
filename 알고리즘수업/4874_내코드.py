import sys
sys.stdin = open("4874.txt", "r")

T = int(input())
for tc in range(1,T+1):
    stack = []
    temp = input().split() #list로만 받기
    N = len(temp)
    errorflag = 0;
    #숫자와 연산자 케이스를 나누어서 stack에 받음

    for i in range(N-1): #.전까지 처리함
        try:
            if temp[i].isdigit():
                stack.append(temp[i])
            else: #연산자 일때
                num1, num2 = int(stack.pop()), int(stack.pop())
                if temp[i] == '+': result = num2 + num1
                elif temp[i] == '-': result = num2 - num1
                elif temp[i] == '*': result = num2 * num1
                elif temp[i] == '/': result = num2 // num1
                stack.append(result)

        except:
            errorflag = 1

    if len(stack) == 1 and errorflag == 0: #왜 1이 아니면 하면 다 여기로 안들어와?
        print('#%d %d' % (tc,stack[0]))
    elif len(stack) != 1 or errorflag == 1:
        print('#%d %s' % (tc,'error'))
