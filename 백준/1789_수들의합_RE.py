import sys
sys.stdin = open('input.txt','r')


# leetcode 33번과 뭐가 달라?
# 33번은 값이 있고, 임의적으로 나눈 두 검색 범위 중 어디에 들어가냐의 문

# 여기선, target가 S와 일치하는 순간 없을 수 있음.
# 특히, s,e가 +1로 좁혀지면 mid가 계속 똑같고 무한루프가 돈다.


if __name__ == '__main__':
    S = int(input())
    s,e = 0, S
    ans = 0
    while s<=e:
        cnt = (s+e)//2
        target = ((cnt+1)*cnt)//2
        if target <= S:
            s = cnt+1
        else:
            e = cnt-1
            ans = e
    print(ans)
