import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        n=int(input())
        cnt=0
        for idx,val in enumerate(bin(n)[2:][::-1]):
            if val=='1':
                print(idx,end=' ')



