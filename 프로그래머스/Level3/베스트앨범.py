from collections import defaultdict

def solution(genres, plays):
    D = defaultdict(list)
    for idx, genre in enumerate(genres):
        D[genre] += [(plays[idx],-idx)] 
    sorted_key = sorted(D, key = lambda key : sum([i[0] for i in D[key]]), reverse=True)
    ans=[]
    for key in sorted_key:
        for _ in range(2):
            if D[key]: # 
                maxv = max(D[key]) # 단일 값을 기준으로 해. sort처럼. 튜플이어도 오름차순 왼ㅈ차순
                ans.append(-maxv[1])
                D[key].remove(maxv)

    return ans