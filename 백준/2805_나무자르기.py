import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    s = 0
    e = max(N_list)
    ans = s
    while s<=e:
        target = (s+e)//2
        cuts = 0
        for i in range(N):
            if N_list[i] > target:
                cuts+=(N_list[i]-target)
        if cuts>=M: #너무잘랐다. 높이를 더 늘려야 한다.
            s = target+1
            ans = max(ans,target)
        else: #덜잘랐다. 높이를 줄여야 한다.
            e = target -1
    print(ans)
