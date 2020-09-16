import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,C = map(int, input().split())
    N_list = [int(input()) for _ in range(N)]
    N_list.sort()
    s = 1 # 최소간격은 1
    e = N_list[-1]-N_list[0] # 최대간격은 가장 큰 좌표와 작은 좌표의 간격
    while s<=e:
        target = (s+e)//2
        start = N_list[0]
        group = 1
        for i in range(1,N): #lower bound 이므로 최소간격. 가장 인접한 애의 간격을 구해야 하므로.
            if N_list[i]-start >= target:
                group += 1
                start = N_list[i]
        if group >= C: # 간격이 너무 작았다. 간격을 키워야 한다.
            s = target+1
            ans = target # ans는 더 커진 값이 담기게 된다.
        else:
            e = target-1
    print(ans)
