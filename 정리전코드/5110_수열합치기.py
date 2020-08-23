import sys
sys.stdin = open("input.txt", "r")

def merge(l):
    global result
    for i in range(1,N): #l-1개인 이유는? - 두 수 사이에서 merge이므로
        sq_1 = result #덮어쓰기
        sq_2 = l[i]

        target = sq_2[0]
        idx = -1 #######
        for s in sq_1:
            if s > target:
                idx = sq_1.index(s)
                break
        if idx == -1:
            result.extend(sq_2)
        else:
            result[idx:0] = sq_2
    return result

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    l = [0]*M
    for i in range(M):
        l[i] = list(map(int, input().split()))
    result = l[0]
    temp = merge(l)
    string = ''
    for k in temp[len(temp)-1:-11:-1]:
        string += str(k)
        string += ' '
    print('#%d %s' % (tc,string))