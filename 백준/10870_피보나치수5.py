import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    n=int(input())
    D=[0]*21
    D[1]=1
    D[2]=1
    for i in range(3,n+1):
        D[i]=D[i-1]+D[i-2]
    print(D[n])