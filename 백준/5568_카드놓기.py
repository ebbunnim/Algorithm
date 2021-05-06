import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def permu(cnt,res):
    if cnt==k:
        candidates.add(res)
        return

    for i in range(n):
        if vis[i]==False:
            vis[i]=True
            permu(cnt+1,res+str_list[i])
            vis[i]=False
    return

if __name__=="__main__":
    n=int(input().strip())
    k=int(input().strip())
    vis=[False]*n
    str_list=[input().strip() for _ in range(n)]
    candidates = set()
    permu(0,'')
    print(len(candidates))
