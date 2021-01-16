import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    maxlist=arr[0]
    minlist=arr[0]

    for r in range(1,N):
        c1=max(maxlist[0],maxlist[1])+arr[r][0]
        c2=max(maxlist[0],maxlist[1],maxlist[2])+arr[r][1]
        c3=max(maxlist[1],maxlist[2])+arr[r][2]
        maxlist=[c1,c2,c3]

        c1 = min(minlist[0], minlist[1]) + arr[r][0]
        c2 = min(minlist[0], minlist[1], minlist[2]) + arr[r][1]
        c3 = min(minlist[1], minlist[2]) + arr[r][2]
        minlist=[c1,c2,c3]

    print(max(maxlist),min(minlist))