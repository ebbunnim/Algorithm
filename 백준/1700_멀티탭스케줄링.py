import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline
from collections import Counter

if __name__ == '__main__':
    N,K=map(int,input().split())
    plugs=list(map(int,input().split()))
    counter=Counter(plugs)
    window=set()
    l=0
    cnt=0
    for i in range(K):
        plug=plugs[i]
        counter[plug]-=1
        if plug in window:
            continue
        if l<N:
            window.add(plug)
            l+=1
        else:# l==N 순간 이후
            flag=0
            for ele in window:
                if counter[ele]<=0:
                    final_ele=ele
                    flag=1
                    break
            if not flag:
                # 가장 마지막에 있는애? NO(->현재시점 기준으로 바로 다음에 등장할 때 가장 멀리있는 애)
                max_idx=0
                final_ele=0
                for ele in window:
                    idx=plugs[i:].index(ele)
                    if idx>max_idx:
                        max_idx=idx
                        final_ele=ele
            window.discard(final_ele)
            window.add(plug)
            cnt += 1
    print(cnt)


# 윈도우에 있는 녀석일 경우
    # 무시
# 윈도우에 없는 녀석일 경우에는
    # N을 채우지 못했다면 그냥 넣는다.
    # N을 채웠다면, 한 녀석을 버려야 한다.
        # 더 이상 쓰지 않는 녀석 out
        # 다 한번 이상 써야한다면 현재 위치 기준으로 가장 나중에 등장하는 원소 (그리디인 이유. 만약에 현재 위치 기준이 아니라 가장 마지막에 위치한 원소로 탐색했다면 이전에 등장했을 때 또 바꿨어야 함. 카운트 불가. 따라서 부분해가 최적해를 보장한다는 식으로 풀어야 함. )



# OS에 페이지 교체 전략 중 최적(Optimal) 페이지 교체 방법이 있다.
# 바로 앞으로 가장 오랫동안 사용 되지 않을 페이지를 교체하는 전략이다.
# 가장 페이지 교체 수가 적은 전략이지만 프로세스가 앞으로 사용할 페이지를 알지 못하기에 구현이 불가능하다.
# 하지만 현재 문제는 사용 순서가 정해져 있기 때문에 이 알고리즘을 사용하여 문제를 해결할 수 있다.