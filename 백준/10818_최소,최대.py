import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    maxv,minv=-10**6, 10**6
    Nlist=list(map(int,input().split()))
    for e in Nlist:
        if maxv<e:
            maxv=e
        if minv>e:
            minv=e
    print(minv,maxv)