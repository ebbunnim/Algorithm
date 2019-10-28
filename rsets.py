# import sys
# sys.stdin = open("input.txt","r")
#

icp = {'*':2,'/':2,'+':1,'-':1,'(':3}
isp = {'*':2,'/':2,'+':1,'-':1,'(':0}
token=[]
que=[]
string = '3+(4+5)*6+7'

for s in string:
    if s.isdigit():
        que.append(s)
    else: #연산자라면
        if not token:
            token.append(s)
        elif token:
            if s == ')':
                while token[-1] != '(':
                    a = token.pop()
                    que.append(a)
                token.pop() #'(' while문 탈출 후 삭제까지
            elif isp[token[-1]] < icp[s]:
                token.append(s)
            else: #우선순위 작은 연산자들이라면 계속 pop
                while icp[s] <= isp[token[-1]]:
                    a = token.pop()
                    if not token:
                        que.append(a)
                        break
                    que.append(a)
                token.append(s) #이건 왜? 우선순위 작은애 token에 넣는게 수반돼야
# a = token.pop()
# que.append(a)
stack = []

for q in que:
    if not stack:
        stack.append(q)
    elif stack:
        if q.isdigit():#숫자가 들어오면
            q = int(q)
            stack.append(q)
        else: #연산자가 들어오면
            a = int(stack.pop())
            b = int(stack.pop())
            if q == '*':
                result = b*a
            elif q == '/':
                result = b/a
            elif q == '+':
                result = b + a
            elif q == '-':
                result = b - a
            stack.append(result)
final = stack.pop()
print(final)
