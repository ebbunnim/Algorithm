from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[False]*len(grid[0]) for _ in range(len(grid))]
        
        def bfs():
            Q = deque()
            Q.append((i,j))
            vis[i][j]=True
            
            while Q:
                r, c = Q.popleft()
                for dr, dc in (-1,0),(1,0),(0,-1),(0,1):
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc]==False and grid[nr][nc]=="1":
                        vis[nr][nc]=True
                        Q.append((nr,nc))
            return 1
        
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and vis[i][j]==False:
                    res+=bfs()
        return res
                