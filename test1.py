import sys
sys.stdin = open("input.txt","r")

def backtracking(i): #i는 백트래킹의 시작점
    global ans, cnt, now

    if cnt > ans:
        return
    for jump in range(arr[i], 0, -1): # 만약에 arr[i]=3이면, 3,2,1만큼 뛰겠다. 이게 최소 cnt라면, break함.
        i += jump
        cnt += 1
        if i >= N-1:
            if cnt < ans:
                ans = cnt
            cnt-=1; i-=jump
            continue
        backtracking(i)
        cnt -= 1; i-= jump


if __name__ == "__main__":
    T = int(input())
    T = 1
    for tc in range(1, T+1):
        temp = list(map(int, input().split()))
        print(temp)
        N = temp[0]
        arr = [0]*N
        for i in range(1, N):
            arr[i-1] = temp[i]
        # 현재의 위치에서 arr에 담긴(내용은 idx 정류장에서 arr의 수만큼 갈 수 있다)
        print(arr)
        cnt=0; ans=999999; now=0;
        backtracking(0)
        print('#%d %d' % (tc,ans-1))

