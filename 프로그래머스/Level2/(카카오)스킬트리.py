def solution(skill, skill_trees):
    ans = 0
    N = len(skill)
    for tree in skill_trees:
        D = [30]*26
        idx = 1
        for a in tree:
            D[ord(a)-65] = idx
            idx += 1
        flag = 0
        for i in range(N-1): # skill과 순위 오름차순 비교
            if D[ord(skill[i])-65] <= D[ord(skill[i+1])-65]:
                pass
            else:
                flag =1
                break
        if flag == 0:
            ans += 1
    return ans