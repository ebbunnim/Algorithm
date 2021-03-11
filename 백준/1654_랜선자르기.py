import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def bs():
    s,e=0,2**31
    while s<e:
        mid=(s+e)//2
        cnt=0
        for length in lengths:
            cnt+=(length//mid)
        if cnt>=N: # 최대 길이를 더 늘릴 수 있다.
            s=mid+1
        else:
            e=mid
    return e

if __name__ == '__main__':
    K,N=map(int,input().split())
    lengths=[int(input()) for _ in range(K)]
    print(bs()-1)