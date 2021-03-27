def solution(a):
    n=len(a)
    res=[1]*n
    minv1=10**9+1
    minv2=10**9+1
    # left -> right
    for i in range(n):
        if minv1<a[i]:
            res[i]-=1
        else:
            minv1=a[i]
    # right -> left
    for i in range(n-1,-1,-1):
        if minv2<a[i]:
            res[i]-=1
        else:
            minv2=a[i]
    return sum([1 for ele in res if ele!=-1])