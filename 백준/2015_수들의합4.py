import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')


from collections import defaultdict

# 연속된 부분합 아니다.
# prefix sum + 만들 수 있는 경우의
if __name__ == '__main__':
    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    D = defaultdict(int)

    psum = 0
    ans = 0
    for idx,num in enumerate(N_list):
        psum += num
        if D[psum-K]:
            ans += D[psum-K]
        D[psum]+=1
    print(ans+D[K])

    # D : key가 만들어진 횟수.