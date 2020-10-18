from collections import defaultdict,Counter

def solution(N, stages):
    counter = Counter(stages)
    fails = defaultdict(int)
    total = len(stages)
    for i in range(1,N+1): # asc
        if total!=0:
            fails[i]=counter[i]/total
            total -= counter[i]
        else:
            fails[i]=0
    return sorted(fails,key=lambda x : fails[x],reverse=True)