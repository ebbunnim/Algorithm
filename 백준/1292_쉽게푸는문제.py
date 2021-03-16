import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    A,B=map(int,input().split())
    Nlist=[0]
    for i in range(1,B+1):
        Nlist+=[i]*i
    psum=[e for e in Nlist]
    for i in range(1,B+1):
        psum[i]+=psum[i-1]
    print(psum[B]-psum[A-1])

