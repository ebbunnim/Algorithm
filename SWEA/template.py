import sys
sys.stdin = open('input.txt','r')

if __name__=="__main__":
    for t in range(int(input())):
        N = int(input())
        Nlist = list(map(int,input().split()))

        print(f'#{t+1}')



