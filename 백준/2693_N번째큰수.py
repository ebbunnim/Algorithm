import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        Nlist=list(map(int,input().split()))
        Nlist.sort()
        print(Nlist[7])

