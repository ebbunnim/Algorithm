import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')

if __name__ == '__main__':
    N = int(input())
    Nlist = list(map(int,input().split()))

    # s, e : s -> e <- 값이 작아지면 계속 갱신, ans에도
    # e만 쭉오면서 갱신하다가.
    # e만 쭉오면서 갱신하다가. 더한 값(0과의 절대값)이 0 보다 작아지는 순간이 생기면,  s를 움직인다.
    s, e = 0, N-1
    diff = 2000000000
    while s<e:
        sumv = Nlist[s]+Nlist[e]
        if abs(sumv) < diff:
            diff = abs(sumv)
            ans = (s,e)
        if sumv > 0:
            e -= 1
        else:
            s += 1

    print(Nlist[ans[0]],Nlist[ans[1]])



