n = 13
nlist = [1, 1, 1, 2, 2, 2, 2, 3, 3 ,3, 5,8,8]

# target보다 작거나 같은 수를 찾는다.
def BS_lower_bound(target):
    s, e = 0, n-1
    while s<e:
        mid = (s+e)//2
        if nlist[mid]>=target:
            e = mid
        else:
            s = mid + 1
    return e

# target보다 큰 수를 찾는다.
def BS_upper_bound(target):
    s, e =0, n-1
    while s<e:
        mid = (s+e)//2
        if nlist[mid]>target:
            e = mid
        else:
            s =mid + 1
    return e

# 없는 수에 대해서는 더 큰 수 찾고 똑같은 인덱스가 출력됨
print(BS_lower_bound(4)) # 10
print(BS_upper_bound(4)) # 10
# 3의 인덱스를 찾되, 동일값에 대해서는 가장 왼쪽 끝 인덱스
# 3보다 큰 수가 있으므로 그 인덱스를 찍
print(BS_lower_bound(3)) # 7
print(BS_upper_bound(3)) # 10
# 8의 인덱스를 찾되, 동일값에 대해서는 가장 왼쪽 끝 인덱스
# 더 큰 값 찾을려고 해도, 못찾으면 8 인덱스를 호출함.  동일한 8이 있을 때 가장 오른쪽 끝 인덱스
print(BS_lower_bound(8)) # 11
print(BS_upper_bound(8)) # 12

print(BS_lower_bound(1)) # 0
print(BS_upper_bound(1)) # 3
# Nlist모든 원소보다 더 작은/큰값을 찾을때는 양 끝의 인덱스 출력하게 됨