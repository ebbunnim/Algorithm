import sys
sys.stdin = open('input.txt','r')

if __name__=="__main__":
    for t in range(int(input())):
        N = int(input())
        Nlist = list(map(int,input().split()))

        stack = []
        benefits = 0

        # stack에서 아예 꺼내는게 아니라, 계속 누적해. 그러면 차라리 뒤에서부터 maxv 두고 차이 구하는게 낫다.
        maxv = 0
        for i in range(N-1,-1,-1):
            maxv = max(maxv, Nlist[i])
            benefits+=(maxv-Nlist[i])

        print(f'#{t+1} {benefits}')





