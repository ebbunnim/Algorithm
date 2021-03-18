import sys
sys.stdin = open('input.txt','r')

def dfs(i):
    if i==15:
        for i in range(6):
            for j in range(3):
                if arr[i][j]!=0:
                    return 0
        return 1

    src,dst=rival1[i],rival2[i]

    # 3개의 가지. 승/무/패
    if arr[dst][2] and arr[src][0]:
        arr[dst][2]-=1
        arr[src][0]-=1
        if dfs(i+1):
            return 1
        arr[src][0]+=1
        arr[dst][2]+=1

    if arr[dst][1] and arr[src][1]:
        arr[dst][1]-=1
        arr[src][1]-=1
        if dfs(i+1):
            return 1
        arr[src][1]+=1
        arr[dst][1]+=1

    if arr[dst][0] and arr[src][2]:
        arr[dst][0]-=1
        arr[src][2]-=1
        if dfs(i+1):
            return 1
        arr[src][2]+=1
        arr[dst][0]+=1
    return 0

if __name__ == '__main__':
    rival1=[0,0,0,0,0,1,1,1,1,2,2,2,3,3,4]
    rival2=[1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]
    # 다음번 결과는 이전과 독립적임. a가 b를 이겼다고 해도, b가 c에게 졌을 것이란 제약 없음
    for _ in range(4):
        arr=[[0,0,0] for _ in range(6)] # 승무패
        nlist=list(map(int,input().split()))
        idx=0
        for i in range(6):
            arr[i][0]=nlist[idx]
            arr[i][1]=nlist[idx+1]
            arr[i][2]=nlist[idx+2]
            idx+=3
        print(dfs(0),end=' ')
