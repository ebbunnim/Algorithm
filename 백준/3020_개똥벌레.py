import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N, H = map(int, input().split())
    bottom = []
    top = []
    for i in range(N):
        if i%2==0:
            bottom.append(int(input()))
        else:
            top.append(int(input()))

    bottom.sort()
    top.sort()

    # 찾아야 하는 것 : 각 층에서 몇 개의 장애물을 파괴했냐
    # x를 찾으면, x보다 더 큰 값들의 개수가 최소로 파괴되는 장애물들. - linear하게 갯수를 카운트한다.
    ans = []
    for bound in range(1,H+1):
        # 최소한의 장애물을 cnt 해야 함.
        s, e = 0, len(bottom)-1
        ans1 = 0
        while s<=e:
            mid = (s+e)//2 # 인덱스
            if bottom[mid] >= bound:
                ans1 = len(bottom)-mid # 파괴하는 최소 장애
                e = mid - 1
            else:
                s = mid + 1

        s,e = 0, len(top)-1
        ans2 = 0
        while s<=e:
            mid = (s+e)//2
            if H-top[mid] < bound:
                ans2 = len(top)-mid
                e = mid-1
            else:
                s = mid + 1
        ans.append(ans1+ans2)
    print(ans.count(min(ans)))