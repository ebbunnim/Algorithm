import sys
sys.stdin = open('input.txt','r')

from collections import defaultdict
if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    N_list.sort()
    D = defaultdict(int)
    for i in range(N):
        D[N_list[i]] += 1
    for i in range(M):
        target = M_list[i]
        s = 0
        e = N-1
        flag =0
        while s <= e:
            mid = (s+e)//2
            if N_list[mid] > target:
                e = mid -1
            elif N_list[mid] == target:
                flag = 1
                break
            else:
                s = mid + 1
        if flag == 1:
            print(D[target],end=' ')
        else:
            print(0, end=' ')
