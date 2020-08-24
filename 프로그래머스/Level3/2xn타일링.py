
def solution(n):
    D = [0]*60001
    D[1] = 1
    D[2] = 2
    for i in range(3,n+1):
        D[i] = (D[i-1]+D[i-2])%1000000007
    return D[n]