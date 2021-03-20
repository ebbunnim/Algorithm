import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def calc(): # 효능과 색 모두 하기
    return

def rotate(arr): #시계방향 턴 
    res=[]
    for j in range(4):
        tmp=[]
        for i in range(4):
            tmp+=[arr[i][j]]
        res.append(tmp[::-1])

def rotate2(arr): #반시계방향 턴
    res=[0]*4
    for j in range(4):
        tmp=[]
        for i in range(4):
            tmp+=[arr[i][j]]
        res[3-j]=tmp


if __name__ == '__main__':
    n=int(input())
    ingredients=[]
    for _ in range(n):
        efficiency=[list(map(int,input().split())) for _ in range(4)]
        color=[input().split() for _ in range(4)]
        arr=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                arr[i][j]=[efficiency[i][j],color[i][j]]
        ingredients.append(arr)
    # print(*ingredients[0],sep='\n')

    rotate2(ingredients[0])

# 1. 순열 (재료 선택 - 배치에 뭐가 왔느냐에 따라서 달라지므로 )
# 1-2. 순열의 한 케이스마다 재료들을 돌려봐야(재료마다 4번의 로테이트가 가능하다)
# 1-3. 해당 케이스만 0~9 범위 작업까지 함께 해줘야 한다.
# 1-4. 이때, 효능은 위의 작업이고 색 작업도 함께 해준다.
# 2. 품질의 최대값을 갱신해나간다.