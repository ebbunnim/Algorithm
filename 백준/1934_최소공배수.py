import sys
sys.stdin = open('input.txt','r')

def gcd(N,M):
    r=N%M
    if r==0:
        return M
    return gcd(M,r)

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        N,M=map(int,input().split())
        print(N*M//gcd(N,M))