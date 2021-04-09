import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    T=1
    while True:
        L, P, V = map(int, input().split())
        if not L and not P and not V:
            break
        q,r=divmod(V,P)
        if r>L:
            r=L
        print(f'Case {T}: {L*q+r}')
        T+=1

        # 반례 123 456 789 (답:246)