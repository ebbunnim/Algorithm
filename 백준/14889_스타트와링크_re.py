def count_bit(N):
    cnt=k=0
    while N>=(1<<k):
        if N&(1<<k):
            cnt+=1
        k+=1
    return cnt

def solve(N,M):
    minv=1e9
    for i in range((1<<N)//2):
        if count_bit(i)!=M:
            continue
        start,link=[],[]
        for j in range(N):
            if (i&(1<<j)):
                start+=[j]
            else:
                link+=[j]
        s=l=0
        for i in range(M):
            for j in range(M):
                s+=arr[start[i]][start[j]]
                l+=arr[link[i]][link[j]]
        minv = min(minv,abs(s-l))
    return minv

if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N,N//2))
