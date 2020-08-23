import sys
sys.stdin = open("input1.txt","r")

#
# def Dup():

if __name__=="__main__":
    N=int(input());
    l=[[0]*101 for _ in range(101)] #array를 만든다.
    cnt_1=[0]*(N+1) #여유공간을 하나 더 만든 이유는 back할 공간이 필요하기도 + 0외의 idx 필요했으므로

    for k in range(1,N+1):
        temp=list(map(int,input().split()))
        for i in range(temp[0], temp[0]+temp[2]): #index는 하나가 작은게 맞다. range끝에서 걸러짐
            for j in range(temp[1], temp[1]+temp[3]):
                if l[i][j] != 0:
                    cnt_1[k-1] -= 1
                l[i][j]=k
                cnt_1[k] += 1

    print(cnt_1[1])
    print(cnt_1[2])


#1)idx 로 각 array에 접근했어야 하는게
#2)만약에 k=0부터 시작한다면, 지나온 길을 명시할 수 없다. (0일때 이전 cnt에서 -1해줘야 하는데
#이 케이스에서 인식못하면 답이 다르게 나옴.)

#index는 len-1만큼까지 존재하므로, for문으로 돌리면 range에서 알아서 걸러짐