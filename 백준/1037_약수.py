import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=list(map(int,input().split()))
    maxv,minv=0,sys.maxsize
    for e in Nlist:
        if e>maxv:
            maxv=e
        if e<minv:
            minv=e
    print(minv*maxv)