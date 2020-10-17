import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N = int(input())
    Nlist = list(map(int, input().split()))
    Nlist.sort()
    if N%2: # 홀수
        print(Nlist[N//2])
    else:
        print(Nlist[N//2-1])
