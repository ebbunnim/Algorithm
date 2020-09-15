import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    N_list.sort()
    for i in range(M):
        target = M_list[i]
        s = 0
        e = N-1
        flag = 0
        while s<=e:
            mid = (s+e)//2
            if N_list[mid] < target:
                s = mid + 1
            elif N_list[mid]==target:
                flag = 1
                break
            else:
                e = mid - 1
        if flag == 1:
            print(1,end=' ')
        else:
            print(0,end=' ')
