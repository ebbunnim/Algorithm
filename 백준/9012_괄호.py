if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        L = list(input())
        stack = []
        flag = 0
        for i in range(len(L)):
            if L[i] == '(':
                stack.append(L[i])
            else:
                if stack:
                    stack.pop()
                else:
                    flag = 1
                    print('NO')
                    break
        if flag == 0:
            if stack == []:
                print('YES')
            else:
                print('NO')