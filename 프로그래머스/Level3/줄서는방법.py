from math import factorial

def solution(n, k):
    n_list = [i for i in range(1,n+1)]
    stack = []
    # k는 슬라이스, 몫은 번수.
    while n!= 0:
        cycle = factorial(n-1)
        curr = (k-1)//cycle #k가 0이면 -1이 됨
        k%=cycle
        if k == 0:
            k = cycle # 이게 중요함.
        stack.append(n_list.pop(curr))
        n -= 1
    return stack