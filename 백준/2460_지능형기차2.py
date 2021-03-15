import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    res=0
    maxv=0
    for _ in range(10):
        a,b=map(int,input().split())
        res+=(b-a)
        if res>maxv:
            maxv=res
    print(maxv)