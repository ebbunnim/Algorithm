def solution(dirs):
    dir_dic={
        'L':(0,-1),
        'R':(0,1),
        'U':(-1,0),
        'D':(1,0)
    }
    cr,cc=0,0
    ans=0
    vis=set()
    for d in dirs:
        dr,dc=dir_dic[d]
        nr,nc=cr+dr,cc+dc
        if -5<=nr<=5 and -5<=nc<=5:
            a,b=sorted([(cr,cc),(nr,nc)])
            if (a,b) not in vis:
                vis.add((a,b))
                ans+=1
            cr,cc=nr,nc
    return ans

# 유용한 반례 : 'LRLRL' 1
