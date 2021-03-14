import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    i=2
    while i<=N:
        if not N%i:
            N=N//i
            print(i)
        else:
            i+=1
