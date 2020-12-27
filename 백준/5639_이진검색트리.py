import sys
sys.setrecursionlimit(10**9)

def postorder(s, e):
    if s > e:
        return
    root = nlist[s]
    div_idx = e + 1  # 원소 하나일때(s==e) 역전시켜 버리기
    for i in range(s + 1, e + 1):
        if nlist[i] > root:
            div_idx = i
            break
    postorder(s + 1, div_idx - 1)
    postorder(div_idx, e)
    print(nlist[s])  # s==e인 상태

if __name__ == '__main__':
    nlist =[]
    while True:
        try:
            nlist.append(int(input()))
        except:
            break
    postorder(0,len(nlist)-1)