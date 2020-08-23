from copy import deepcopy

if __name__ == '__main__':
    text = list(input())
    I = []
    stack = []
    start = []
    for i in range(len(text)):
        if text[i] == '(':
            stack.append('(')
            start.append(i)
            end = i
        elif text[i] == ')':
            I.append((start.pop(), i))
    N = len(I)

    L = []
    for i in range(1,1<<N):
        tmp = deepcopy(text)
        for j in range(N):
            if i & (1<<j):
                # print(I[j])
                tmp[I[j][0]] = '.'
                tmp[I[j][1]] = '.'
        res = ''
        for t in tmp:
            if t != '.':
                res += t
        L.append(res)
    L.sort()
    L = set(L) # 중복제거

    for l in L:
        print(l)
