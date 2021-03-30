def solution(name):
    res=[min(ord(e)-ord('A'),ord('Z')-ord(e)+1) for e in name]
    ans=sum([e for e in res if e])
    n=len(name)
    curr=0
    while True:
        res[curr]=0
        if res==[0]*n:
            break
        dl=dr=1
        while not res[curr-dl]:
            dl+=1
        while not res[curr+dr]:
            dr+=1
        if dl>=dr:
            curr+=dr
            ans+=dr
        else:
            curr-=dl
            ans+=dl
    return ans