# n까지 가서 sum이 가장 작은애를 뽑아야. 얘가 mymin과 계속 값을 갱신해 비교할 submin을 정해야
# visited은 행 기준으로 들어감, for문은 열 기준으로 돌아감. 행과 열이 겹치면 안된다는게 point
# 함수 안에 for문을 써주면 그 행에서 모든 원소를 탐색할 수 있도록 돌아주는 역할을 함.
import sys
sys.stdin = open("4881.txt","r")

def find_min(row):
    global submin, mymin

    if row == n:
        if submin < mymin:
            mymin = submin
        return
    if submin > mymin:
        return


    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            submin += mymap[row][x]
            find_min(row+1) #제약 어떻게?
            visited[x] = 0
            submin -= mymap[row][x]



if __name__=="__main__":
    T = int(input())
    for tc in range(1, T + 1):
        n = int(input())
        mymap = [list(map(int, input().split())) for _ in range(n)]
        submin = 0;
        mymin = 9999999;
        visited = [0] * n  # 행 기준
        find_min(0)  # 여기에 넣은 0은 row 기준
        print('#%d %d' % (tc, mymin))