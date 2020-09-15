import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,M = map(int, input().split())
    N_list = list(map(int,input().split()))
    # 1. start, end를 어디까지?
    s = max(N_list) # (주의) 트랙의 길이를 반으로 쪼개면 안된다.
    e = sum(N_list)
    ans = e
    while s <= e:
        target = (s+e)//2
        group = 0
        subsum = 0
        for i in range(N):
            if subsum + N_list[i] <= target:
                subsum += N_list[i]
            else:
                subsum = N_list[i]
                group += 1
        group += 1

        if group <= M: # 작아도, 더 작을 수 있는지 확인한다.
            e = target -1
            ans = min(ans, target)
        else:
            s = target + 1
    print(ans)
