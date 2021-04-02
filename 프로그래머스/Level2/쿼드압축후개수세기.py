
def solution(arr):
    def dv_and_coq(r,c,n):
        # base case
        if n==1:
            return [0,1] if arr[r][c] else [1,0]
        # devide
        m=n//2
        lu=dv_and_coq(r,c,m)
        ru=dv_and_coq(r,c+m,m)
        ld=dv_and_coq(r+m,c,m)
        rd=dv_and_coq(r+m,c+m,m)
        # conquer and merge
        if lu==ru==ld==rd==[0,1] or lu==ru==ld==rd==[1,0] : # compress하기 위해서는 모두 0이거나 1로 대표되었어야 한다.
            return lu # 대표값 하나 올려보내는 압축의 의미
        else:
            return list(map(sum,zip(lu,ru,ld,rd)))
    return dv_and_coq(0,0,len(arr))

# 반환해야 하는 값 - [0,0] => 0개는 0번 인덱스에, 1은 1번 인덱스에 넣어야 한다.
# 부분합 => 전체 합을 올려줘야 하니까 계속 상위로 올려줘야 한다.