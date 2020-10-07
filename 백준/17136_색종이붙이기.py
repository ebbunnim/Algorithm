import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')


if __name__ == '__main__':
    arr = [list(map(int, input().split())) for _ in range(10)]
    papers = [0, 5, 5, 5, 5, 5] # i에는 i*i 크기의 색종이
    minv = 26
    # size에 따라 색종이 붙일 수 있는지 확인
    def can_attach(r,c,size):
        for i in range(r,r+size):
            for j in range(c,c+size):
                if 0<=i<10 and 0<=j<10 and arr[i][j] == 1:
                    pass
                else:
                    return False
        return True

    # update paper, attach or remove
    def update_paper(r,c,size,method): #  attach = 0, remove = 1
        for i in range(r,r+size):
            for j in range(c,c+size):
                arr[i][j] = method

    def dfs(cnt):
        global minv

        # prunning
        if cnt > minv:
            return

        F = 0
        for i in range(10): # search start point
            for j in range(10):
                if arr[i][j] == 1:
                    r, c = i, j
                    F = 1
                    break
            if F==1:
                break

        # start point가 더 이상 없다면 리턴
        if F==0:
            if cnt < minv:
                minv = cnt
            return

        for size in range(5,0,-1): #5,4,3,2,1 => 루트노드이자, 순회 순서. 재귀로 다시 호출되면 현재 루트 노드의 하위 요소를 순회
            if papers[size]>0 and can_attach(r,c,size):
                update_paper(r,c,size,0)
                papers[size]-=1
                dfs(cnt+1)
                update_paper(r,c,size,1)
                papers[size]+=1

    dfs(0)

    if minv == 26:
        print(-1)
    else:
        print(minv)


# vis : 값을 변경하지 않고 중복없이 확인해야 하면 썼어야 됐음. 혹은 노드를 중복되게 호출하는 걸 막거나