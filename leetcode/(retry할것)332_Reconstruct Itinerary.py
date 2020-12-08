from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True) #sort()로 그냥 할거면 아래 pop(0) 필요
        D=defaultdict(list)
        for ticket in tickets:
            D[ticket[0]]+=[ticket[1]]
        
        path=[]
        def dfs(curr,path):
            while D[curr]:
                dfs(D[curr].pop(),path)
            path+=[curr]       
        dfs('JFK',path)
        return path[::-1]
        
