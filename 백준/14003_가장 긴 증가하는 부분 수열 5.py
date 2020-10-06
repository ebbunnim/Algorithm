import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')

# 1 5 10 4 에서 1 4 10 은 오답이다. 최장 수열 구성요소를 묻는다면 tracing 과정이 추가되어야 한다(like union-find)
if __name__ == '__main__':
    N = int(input())
    Nlist = list(map(int, input().split()))
    D=[0] # 처음에는 무조건 0인덱스 수가 추가됨
    T =[-1]*N # 자신보다 앞에 있는 애의 인덱스를 담는다. 0 이 호출되면 find parent 끝내기 위해 -1로 초기화

    # lowerbound 같거나 작은 수를 찾고, 밀어내기 위함.
    def binary_search(n):
        s, e = 0, len(D)-1
        while s<e:
            mid = (s+e)//2
            if Nlist[D[mid]]>=n:
                e = mid
            else:
                s = mid + 1
        return e

    ans = []
    for i in range(1,N):
        if Nlist[D[-1]] < Nlist[i]: # 최장수열을 연이어 생성한다.
            T[i] = D[-1] # D[-1]로 이전 인덱스 저장(tracing) 후 append
            D.append(i)
        else:
            idx = binary_search(Nlist[i]) # 아무리 작아도 0임. D[0]은 바뀔 수가 없다. 이 인덱스는 D 내부의 인덱스
            D[idx] = i # 최장수열을 수정하되, D[idx] 바로 뒤로 연결된 요소는 i를 tracing 함
            if idx != 0: # idx==0 이라면, LIS의 가장 앞이므로 tracing할 부모가 없으므로 pass
                T[i] = D[idx-1] #  # 현대 인덱스를 기준으로, D에 들어있는 원소의 인덱스를 트레이싱 한다.

    n = D[-1] # D[-1]이 붙은 경우가 LIS임. 다만, 1 5 10 4 의 답은 1-4-10이 아닌 1-5-10이므로 10이 5를 trace하도록 만들어 놓았던 것
    while True:
        if n == -1:
            break
        ans.append(Nlist[n])
        n = T[n] # parent tracing
    print(len(ans))
    while ans:
        print(ans.pop(), end=' ')

