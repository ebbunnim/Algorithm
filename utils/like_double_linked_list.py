enter=[3,2,1]
leave=[1,3,2]

from collections import defaultdict

n=len(enter)
post_element=[0]*(1+n)
pre_element=[0]*(1+n)
is_out=[True]+[False]*n
coincidence=defaultdict(set)
process=set()

def make_requirements():
    for i in range(n-1):
        post_element[leave[i]]=leave[i+1]
    for i in range(1,n):
        pre_element[leave[i]]=leave[i-1]

make_requirements()
idx=0
while idx<n:
    curr=enter[idx]
    process.add(curr)
    for ele in process:
        coincidence[ele].update(process) # list extend ~~ set update
    while (curr in process) and is_out[pre_element[curr]]:
        process.discard(curr)
        is_out[curr]=True
        curr=post_element[curr] # like double linked list
    idx+=1
ans=[]
for ele in range(1,n+1):
    ans+=[len(coincidence[ele])-1]
print(ans)

