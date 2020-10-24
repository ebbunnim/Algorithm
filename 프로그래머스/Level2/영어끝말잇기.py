from collections import defaultdict

def solution(n, words):
    answer = [0,0]
    N = len(words)
    D = defaultdict(int)
    end = words[0][-1]
    D[words[0]]=1
    for i in range(1,N):
        if words[i] not in D.keys():
            if end == words[i][0]:
                D[words[i]]=1
                end = words[i][-1]
            else:
                return [i%n+1,i//n+1]
        else:
            return [i%n+1, i//n+1]
    return answer