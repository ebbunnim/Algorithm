
def getcount(name):
    l,o,v,e = 0,0,0,0
    for i in name:
        if ord(i) == 76:
            l += 1
        elif ord(i) == 79:
            o += 1
        elif ord(i) == 86:
            v += 1
        elif ord(i) == 69:
            e += 1
    return l, o, v, e


if __name__ == '__main__':
    l1, o1, v1, e1 = getcount(input())
    N = int(input())
    maxv = 0
    who = '' #  무조건 가장 작은 알파벳으로 취급됨
    for _ in range(N):
        girl = input()
        l2, o2 ,v2, e2, = getcount(girl)
        tmp = ((l1+l2+o1+o2)*(l1+l2+v1+v2)*(l1+l2+e1+e2)*(o1+o2+v1+v2)*(o1+o2+e1+e2)*(v1+v2+e1+e2))%100
        if maxv < tmp :
            maxv = tmp
            who = girl
        elif maxv == tmp: # 같을 땐 이름만 비교해서 알파벳 더 작은 애를 대입
            if who == '': # 처음 분기
                who = girl
            elif who > girl:
                who = girl
    print(who)
