import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr=[0]*N
for i in range(N):
    arr[i] = list(map(int, input().split)
print(*arr, sep='\n')

