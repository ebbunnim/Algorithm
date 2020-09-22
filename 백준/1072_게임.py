import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    X, Y = map(int, input().split())
    initial_Z = (Y*100//X)
    if initial_Z >= 99:
        print(-1)
    else:
        s, e =  0, 1000000000
        while s <= e:
            mid = (s+e)//2
            Z = ((Y+mid)*100)//(X+mid)
            if initial_Z+1 <= Z: #lower bound + min 찾기
                e = mid -1
                ans = mid
            else:
                s = mid + 1
        print(ans)