import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    ports = [0]+list(map(int, input().split()))
    D = [0]+[1]*40000
    for i in range(1,N+1):
        res = 1
        for j in range(i-1,-1,-1):
            if ports[j] < ports[i]:
                res = max(res, D[j]+1)
        D[i] = res
    print(max(D[:N+1]))