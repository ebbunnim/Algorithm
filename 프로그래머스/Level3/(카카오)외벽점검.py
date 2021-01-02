from itertools import permutations
from copy import deepcopy
from collections import deque

def solution(n, weak, dist):
    def check(perm,m):
        ancestor_Q = deque(weak)
        for _ in range(len(weak)):
            Q = deepcopy(ancestor_Q)
            for j in range(m):
                s=Q[0]
                e=s+perm[j]
                while Q:
                    if Q[0]<=e:
                        Q.popleft()
                    else:
                        break
            if not Q:
                return m
            ancestor_Q.append(ancestor_Q.popleft()+n)
        return -1

    dist.sort(reverse=True)
    for i in range(1,len(dist)+1):
        perms=list(permutations(dist,i))
        for perm in perms[:len(perms)//2]:
            if check(perm,i)!=-1:
                return i
    return -1