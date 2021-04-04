import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def func1(arr): # 상하반전
    global N,M
    res=[[] for _ in range(N)]
    for r in range(N-1,-1,-1):
        res[N-1-r]=arr[r]
    return res

def func2(arr): # 좌우반전
    global N,M
    res=func3(arr)
    res=func1(res)
    res=func4(res)
    return res

def func3(arr): # 오른쪽 90도
    global N,M
    res=[]
    for c in range(M):
        tmp=[]
        for r in range(N):
            tmp+=[arr[r][c]]
        res.append(tmp[::-1])
    N,M=M,N
    return res

def func4(arr): # 왼쪽 90도
    global N,M
    res=[[] for _ in range(M)]
    for c in range(M):
        tmp=[]
        for r in range(N):
            tmp+=[arr[r][c]]
        res[M-1-c]=tmp
    N,M=M,N
    return res

def divide_four_section(arr): # 배열 전체 4등분
    global N,M
    mid_N=N//2
    mid_M=M//2
    res=[]
    res.append([arr[row][:mid_M] for row in range(mid_N)])
    res.append([arr[row][mid_M:] for row in range(mid_N)])
    res.append([arr[row][:mid_M] for row in range(mid_N,N)])
    res.append([arr[row][mid_M:] for row in range(mid_N,N)])
    return res

def func5(arr): # 4등분 후 오른쪽 90도 회전
    global N,M
    res=divide_four_section(arr)
    tmp=[]
    tmp.append(res[2])
    tmp.append(res[0])
    tmp.append(res[3])
    tmp.append(res[1])
    result=[]
    for i in range(len(tmp[0])):
        result.append(tmp[0][i]+tmp[1][i])
    for i in range(len(tmp[2])):
        result.append(tmp[2][i]+tmp[3][i])
    return result

def func6(arr): # 4등분 후 왼쪽 90도 회전
    global N,M
    res=divide_four_section(arr)
    tmp=[]
    tmp.append(res[1])
    tmp.append(res[3])
    tmp.append(res[0])
    tmp.append(res[2])
    result=[]
    for i in range(len(tmp[0])):
        result.append(tmp[0][i]+tmp[1][i])
    for i in range(len(tmp[2])):
        result.append(tmp[2][i]+tmp[3][i])
    return result

if __name__ == '__main__':
    N,M,R=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    func_idx=list(map(int,input().split()))
    func_list=[func1,func2,func3,func4,func5,func6]
    for idx in func_idx:
        arr=func_list[idx-1](arr)
    for row in arr:
        print(*row)
