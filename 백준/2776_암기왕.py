import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        Nlist = list(map(int, input().split()))
        M = int(input())
        Mlist = list(map(int, input().split()))

        Nlist.sort()
        def binary_search(target):
            s, e = 0, N-1
            while s<=e:
                mid = (s+e)//2
                if Nlist[mid]>target:
                    e = mid -1
                elif Nlist[mid]==target:
                    return 1
                else:
                    s = mid + 1
            return 0

        for target in Mlist:
            print(binary_search(target))