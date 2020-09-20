import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    s,e = 1, K
    while s <= e:
        target = (s+e)//2
        cnt = 0
        for i in range(1,N+1):
            cnt += min(target//i, N)
        if cnt >= K:
            e = target-1
            ans = target
        else:
            s = target + 1
    print(ans)