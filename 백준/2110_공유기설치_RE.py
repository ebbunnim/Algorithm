import sys
sys.stdin = open('input.txt','r')

# 다른 거리들보다 작거나 같은 수 target 찾는다 (lower bound)
# 그 거리가 최대가 될 수 있도록 조정한다. (max)

if __name__ == '__main__':
    N, C = map(int, input().split())
    homes = [int(input()) for _ in range(N)]

    homes.sort()

    def binary_search():  # 간격인 target을 조절해서 target보다 크거나 같은 간격으로 C개의 공유기가 위치할 수 있는지 찾는다.
        s, e = homes[1]-homes[0], homes[-1]-homes[0] # 최소갭, 최대갭. 인덱스 아님
        ans=s # home 딱 두개일 때는 s,e가 같으므로
        while s<e:
            mid = (s+e)//2 # 이 간격으로 몇개까지 커버할 수 있냐?
            start = homes[0] # 최적해를 보장하는 스타트. 첫번째 집에 공유기 설치
            group=1
            for i in range(1,N):
                if homes[i]-start>=mid:
                    group+=1
                    start = homes[i]
            if group >= C: # 간격을 더 벌릴 수 있다.
                s = mid + 1
                ans = mid
            else: # 간격을 줄인다.
                e = mid
        return ans
    print(binary_search())