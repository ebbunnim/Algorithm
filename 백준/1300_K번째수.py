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
    # k라는 숫자는 k번째 수보다 크거나 같다. 1인 경우에 같고 2, 3 ...으로 넘어가면 더 커지게 된다.
    # 우리는 k번째 수 target을 찾아야 하며, cnt 이 숫자보다 작거나 같은 수가 몇개 존재하는지를 알려준다.
    # 따라서, target은 실제로 cnt가 k보다 같거나 큰 범위 내에 존재한다.
