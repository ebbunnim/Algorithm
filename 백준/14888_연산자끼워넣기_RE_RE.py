import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    Nlist = list(map(int, input().split()))
    nums = list(map(int, input().split())) #+-x%
    bohos=[]
    boho=['+','-','x','%']
    vis=[False]*(N-1)
    for i in range(4):
        bohos.extend([boho[i] for _ in range(nums[i])])
    minv,maxv=10**10+1, -10**10-1

    def calc(v1,v2,boho):
        if boho=='+':
            return v1+v2
        elif boho=='-':
            return v1-v2
        elif boho=='x':
            return v1*v2
        elif boho=='%':
            if v1<0 and v2<0:
                return abs(v1)//abs(v2)
            if v1<0 or v2<0:
                return -(abs(v1)//abs(v2))
            return v1//v2

    def permu(stack,cnt):
        global maxv,minv
        if cnt==N-1:
            res=Nlist[0]
            for i in range(N-1):
                res=calc(res,Nlist[i+1],stack[i])
            if res>maxv:
                maxv=res
            if res<minv:
                minv=res
            return

        for i in range(N-1):
            if not vis[i]:
                stack+=[bohos[i]]
                vis[i]=True
                permu(stack,cnt+1)
                vis[i]=False
                stack.pop()

    permu([],0)
    print(maxv)
    print(minv)