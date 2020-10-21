ans = 0
def solution(numbers, target):
    N = len(numbers)
    def dfs(sidx,sumv):
        global ans
        if sidx==N:
            if sumv == target:
                ans += 1
            return
        dfs(sidx+1,sumv+numbers[sidx])
        dfs(sidx+1,sumv-numbers[sidx])
    dfs(0,0) #vis 관리 안할거면 start_idx
    return ans