import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=list(map(int,input().split()))
    res=[0]*N
    # stack에는 인덱스 관리. 값 비교할때는 Nlist로 보기
    s1,s2=[i for i in range(N)], []
    s2.append(s1.pop())
    while s1:
        while s2 and Nlist[s1[-1]]>=Nlist[s2[-1]]:
            res[s2.pop()]=s1[-1]+1
        s2.append(s1.pop())
    print(*res)