import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    ports = [0]+list(map(int, input().split()))
    ans = [0]

    def binary(x, ans):
        s, e = 0, len(ans)-1
        while s <= e:
            mid = (s+e)//2
            if x <= ans[mid]  :
                e -= 1
                res = mid
            else:
                s += 1
        return res



    for i in range(1, N+1):
        if ans[-1] < ports[i]:
            ans.append(ports[i])
        else:
            ans[binary(ports[i],ans)] = ports[i]
    print(len(ans)-1)
