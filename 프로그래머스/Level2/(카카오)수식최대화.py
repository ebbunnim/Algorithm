from copy import deepcopy
from collections import deque
from itertools import permutations


def solution(expression):
    Q = deque()
    s = 0
    for i in range(len(expression)):
        if expression[i] in ['+', '*', '-']:
            Q.append(expression[s:i])
            Q.append(expression[i])
            s = i + 1
    Q.append(expression[s:])  # 마지막까지
    startQ = deepcopy(Q)

    def calculate(a, b, boho):
        a = int(a)
        b = int(b)
        if boho == '+':
            return a + b
        elif boho == '-':
            return a - b
        else:
            return a * b

    bohos = ['*', '+', '-']
    bohos_perm = list(permutations(bohos, 3))
    maxv = 0
    for bohos in bohos_perm:
        Q = deepcopy(startQ)  # 초기화
        for i in range(3):
            boho = bohos[i]
            stack = []
            while Q:
                curr = Q.popleft()
                if curr == boho:
                    n1 = stack.pop()
                    n2 = Q.popleft()
                    stack.append(calculate(n1, n2, boho))
                else:
                    stack.append(curr)
            Q = deque(deepcopy(stack))
        maxv = max(maxv, abs(int(stack[0])))
    return maxv