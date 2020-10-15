import sys
sys.stdin = open('input.txt','r')



if __name__ == '__main__':
    N =int(input())
    ans=0

    def binary_search(t,target): #target이 있는지 없는지만 확인하는 함
        s, e = 0, t
        while s<=e:
            mid = (s+e)//2
            mid_sum = (mid*(mid+1))//2
            if mid_sum > target:
                e = mid -1
            elif mid_sum==target:
                return True
            else:
                s = mid + 1
        return False

    ans = 0
    for t in range(1,N+1):
        subsum = ((t+1)*t)//2
        target = subsum-N
        # 다른 부분합이 target인 애를 찾아야 한다.
        if binary_search(t,target):
            ans += 1
    print(ans)


