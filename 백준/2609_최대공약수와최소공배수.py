import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,M=map(int,input().split())

    def LCM(N,M,gcd):
        return N*M//gcd

    def GCD(N,M):
        r=N%M
        if r==0:
            return M
        return GCD(M,r)

    gcd=GCD(N,M)
    print(GCD(N,M))
    print(LCM(N,M,gcd))

