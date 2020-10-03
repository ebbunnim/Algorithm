import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')


from copy import deepcopy

if __name__ == '__main__':
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def can_set_forward(r,c, val): # col->
        global vis
        copy_vis = deepcopy(vis)
        for i in range(L):
            nc = c + i
            if 0<=nc<N and arr[r][nc]==val and copy_vis[r][nc]==False:
                copy_vis[r][nc] = True
            else:
                return False
        vis = deepcopy(copy_vis)
        return True

    def can_set_forward_by_col(r,c, val): # row ->
        global vis
        copy_vis = deepcopy(vis)
        for i in range(L):
            nr = r + i
            if 0<=nr<N and arr[nr][c]==val and copy_vis[nr][c]==False:
                copy_vis[nr][c] = True
            else:
                return False
        vis = deepcopy(copy_vis)
        return True


    # 열로 만든 길
    vis = [[False]*N for _ in range(N)]
    ans = 0

    for i in range(N):
        flag =0
        cnt = 1
        for j in range(N-1):
            if arr[i][j]==arr[i][j+1]:
                cnt += 1
                continue
            else:
                if arr[i][j]-arr[i][j+1]==1: # 다음부터 오른쪽으로 경사로 놓을 수 있는지 확인한다. (forward)
                    if can_set_forward(i,j+1,arr[i][j+1]):
                        continue
                    else:
                        flag = 1
                        break
                elif arr[i][j]-arr[i][j+1]==-1: # 현재부터 왼쪽으로 경사로 놓을 수 있는지 확인한다. (back)
                    if cnt >= L:
                        for b in range(L):
                            if vis[i][j-b]==False:
                                pass
                            else:
                                flag = 1
                                break
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
                cnt = 1

        if flag == 0:
            ans += 1


    # vis 초기화
    vis = [[False]*N for _ in range(N)]

    # 행으로 만든 길
    for j in range(N):
        flag =0
        cnt = 1
        for i in range(N-1):
            if arr[i][j]==arr[i+1][j]:
                cnt += 1
                continue
            else:
                if arr[i][j]-arr[i+1][j]==1: # 다음부터 아래 경사로 놓을 수 있는지 확인한다. (forward)
                    if can_set_forward_by_col(i+1,j,arr[i+1][j]):
                        continue
                    else:
                        flag = 1
                        break
                elif arr[i][j]-arr[i+1][j]==-1: # 현재부터 위쪽으로 경사로 놓을 수 있는지 확인한다. (back)
                    if cnt >= L:
                        for b in range(L):
                            if vis[i-b][j]==False:
                                pass
                            else:
                                flag = 1
                                break
                    else:
                        flag = 1
                        break

                else:
                    flag = 1
                    break
                cnt = 1

        if flag == 0:
            ans += 1

    print(ans)

