def solution(n):
    T='0123456789ABCDEFG'
    def convert(num,base):
        q,r=divmod(num,base)
        if q==0:
            return T[r]
        else:
            return T[r]+convert(q,base) # 뒤에다가 붙임
    res=convert(n,3)
    return int(str(res),3)

