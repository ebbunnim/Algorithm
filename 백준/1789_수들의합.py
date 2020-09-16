import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    S = int(input())
    # S를 만들되, 최대한 활용하는 수를 많이써라
    # 몇개썼냐?
    # 최대한 수를 늘리려면, 순차적으로 수를 사용해야한다.
    # 찾을 값 - max, min
    # 제한 조건  - lower bound, upper bound로 될 수 있다.
    s = 0
    e = S
    while s <= e:
        mid = (s+e)//2
        sumv = (mid*(mid+1))//2
        if sumv > S:
            e = mid-1
        else: # sumv <= S라고 한다면
            s = mid+1
            ans = mid
    print(ans)
