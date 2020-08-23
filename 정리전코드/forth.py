import sys
sys.stdin = open("input1.txt","r")

T = int(input())
for tc in range(1,T+1):
    que = input().split()
    stack=[]
    for q in que:
        if q == '.':
            if len(stack) != 1:
                final = 'error'
                break
            final = int(stack.pop())

        else:
            if q.isdigit():
                stack.append(int(q))
            elif q == '+' or q == '*' or q == '/' or q == '-' : #연산자를 만나면,
                if len(stack) < 2:
                    final = 'error'
                    break
                a = int(stack.pop())
                b = int(stack.pop())
                if q == '+':
                    result = b + a
                    stack.append(result)
                elif q == '/':
                    result = b // a
                    stack.append(result)
                elif q == '*':
                    result = b * a
                    stack.append(result)
                elif q == '-':
                    result = b - a
                    stack.append(result)
                else:
                    final = 'error'
                    break
            else:
                final = 'error'
                break

    final = str(final)
    print('#%d %s' % (tc,final))