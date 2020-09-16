import sys
sys.stdin = open('input.txt','r')
if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    s = 0
    e = sum(N_list)
    ans = 0
    while s<=e:
        target = (s+e)//2
        subsum = 0
        maxv = 0
        for i in range(N):
            if N_list[i]>target:
                subsum += target
                if target>maxv:
                    maxv = target
            else:
                subsum += N_list[i]
                # if N_list[i]>maxv:
                #     maxv = N_list[i]

        if subsum <= M:
            s = target+1
            ans = max(maxv,ans)
        else:
            e = target-1
    print(ans)
