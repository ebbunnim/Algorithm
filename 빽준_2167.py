import sys
sys.stdin = open("input1.txt","r")

#x, y를 선택하면 x행의 y열의 값까지의 합이 들어있어야(필요하지 않은 부분 빼기)
def DP(arr,x1,y1,x2,y2):
    sum_v = 0
    for row in range(x1, x2+1): #1~3 (1, 1),(1, 2),(1, 3),(2, 1),(2, 2),(2, 3),
        for col in range(y1, y2+1): #1~4
           sum_v += arr[row][col]
    return sum_v

def DP_sum(arr,n,x,y): #x, y를 선택하면 cross로 모든 합 구할 수 있음 (N-1)*(N-1)로 너비차지
    dp = [[0]*n for _ in range(n)]; result=0
    for i in range(N):
        for j in range(N):
            result += arr[i][j]




if __name__ == "__main__":

    N, M = map(int, input().split())
    l=[0]*N
    for n in range(N):
        l[n] = list(map(int,input().split()))
    K = int(input())
    for k in range(K):
        x1,y1,x2,y2 = map(int, input().split())
        result = DP(l,x1-1,y1-1,x2-1,y2-1) #실제로 인덱스 처리할때는 0,0부터 시작하므로
        print(result)

