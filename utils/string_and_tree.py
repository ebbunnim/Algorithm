data=["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
word="SALLY"

# for sort, store start idx where word appears, it can be used for sorting mechanism
def match_search_condition(word:str,name:str,c_id:int)->None or list:
    res=[]
    s=0
    s_sum=0
    while s_sum<len(name):
        idx=name[s:].find(word) # (주의) idx를 독립적으로 관리했어야 함. 예를 들어 슬라이싱 하면 그걸 기준으로 들어가니까 s_sum 관리
        if idx!=-1:
            res+=[idx]
            s=idx+m
            s_sum+=s
        else:
            break
    if s!=0:
        res+=[c_id]
        return res
    return

# make graph and if no child -> then its a leaf node -> dfs로 만든다.
def preprocessing(data:list)->None:
    # make graph, store name, parent info
    for ele in data:
        c_id,name,p_id=ele.split()
        c_id,p_id=int(c_id),int(p_id)
        graph[p_id]+=[c_id]
        names[c_id]=name
        parent[c_id]=p_id
    # determine leaf nodes
    for i in range(1, n + 1):
        if graph[i] == []:
            leaves.add(i)

def make_candidates(word:str,names:list,leaves:set)->(list,list):
    res1=[]
    res2=[]
    for idx,name in enumerate(names): # 1으로 잡아도 enumerate는 바로 인덱스 위치 잡아서 안된다.
        # determine candidates
        if idx in leaves: # only leaf node
            if name==word:
                res1.append([name,idx]) # id, name parent_id 어떤걸 넣어야 하지?
            else:
                tmp=match_search_condition(word,name,idx)
                if tmp:
                    res2.append(tmp)
    return res1,res2

# find parent -> 루트 노드가 가장 마지막에 res에 추가됨에 유의
def find_parent(c_id:int)->None: # 부모 정보는 반대 방향으로 주어진다. 루트까지 가면 가장 마지막에 접근될 것임. 따라서 리스트에 담고 나중에 출력할 때 스트링으로 이어야함
    global res
    if parent[c_id]!=0:
        res+=names[parent[c_id]]+' '
        find_parent(parent[c_id])

n,m=len(data),len(word)
graph=[[] for _ in range(n+1)]
parent=[0]*(n+1) # 0이면 루트다.
names=['']*(n+1)
leaves = set()

# preprocess and make candidates to finally return answer list
preprocessing(data)
res1,res2=make_candidates(word,names,leaves)

# 어떤 케이스든 많이 포함, 앞에 위치한 순, id 오름차순으로 정렬기준을 삼아야 한다.
res1.sort() # word 그대로 들어있어도 id로 선별해야 함.
res2.sort(key=lambda x : (-len(x),x)) # len은 긴 순(==word를 많이 포함한 순)으로 나머지는 그대로 오름차순
tmp=res1+res2 # 모든 원소의 가장 마지막 원소는 id임

# ele로 탐색후에 최종 특징/특징/이름 순으로 가야 한다.
ans=[]
for ele in tmp:
    res=''
    find_parent(ele[-1]) # c_id 넣고 부모 특징까지 넣어둔다.
    parents=res.split()
    path=''
    for p in parents[::-1]:
        path+=p+'/'
    path+=names[ele[-1]]
    ans.append(path)
if ans==[]:
    print([f"Your search for {word} didn't return any results"])
else:
    assert ans==["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"]
    print(ans)

