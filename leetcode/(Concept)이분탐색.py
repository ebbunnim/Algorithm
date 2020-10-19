from bisect import bisect_left, bisect_right

n = 13
nlist = [1, 1, 1, 2, 2, 2, 2, 3, 3 ,3, 5,8,8]

# target보다 작거나 같은 수를 찾는다.
def BS_lower_bound(target):
    s, e = 0, n # 찾으려는 가장 큰 수가 nlist에 없다면, out of index 범위를 가져오지.
    while s<e:
        mid = (s+e)//2
        if nlist[mid]>=target:
            e = mid
        else:
            s = mid + 1
    return e

# target보다 큰 수를 찾는다.
def BS_upper_bound(target):
    s, e =0, n
    while s<e:
        mid = (s+e)//2
        if nlist[mid]>target:
            e = mid
        else:
            s =mid + 1
    return e




# 동일값 처리 예시
print(BS_lower_bound(3)) # 7
print(bisect_left(nlist, 3))
print(BS_upper_bound(3)) # 10
print(bisect_right(nlist, 3))


# 수열 내 가장 큰 수
print(BS_lower_bound(8)) # 11
print(bisect_left(nlist, 8))
print(BS_upper_bound(8)) # 13
print(bisect_right(nlist, 8))

# 수열 내 가장 작은 수
print(BS_lower_bound(1)) # 0
print(bisect_left(nlist, 1))
print(BS_upper_bound(1)) # 3
print(bisect_right(nlist, 1))

# 수열엔 없는 가장 큰수
print(BS_lower_bound(10)) # 13
print(bisect_left(nlist, 10))
print(BS_upper_bound(10)) # 13
print(bisect_right(nlist, 10))

# 수열엔 없는 가장 작은 수
print(BS_lower_bound(0)) # 0
print(bisect_left(nlist, 0))
print(BS_upper_bound(0)) # 0
print(bisect_right(nlist, 0))
