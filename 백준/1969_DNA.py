import sys

if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().split())
    arr = [input() for _ in range(N)]

    ans=''
    cnt = 0

    for j in range(M):
        dic =
        for i in range(N): # 행부터 순회
            dic[arr[i][j]]+=1
        tmp = sorted(dic, key=dic.get, reverse=True)
        ans+=tmp[0]
        for i in range(1,4):
            cnt += dic[tmp[i]]
    print(ans)
    print(cnt)
