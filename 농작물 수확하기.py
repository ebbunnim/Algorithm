import sys
sys.stdin = open("input.txt", "r")

def matprint(arr):
    for i in range(len(arr)):
        print(arr[i])

N = int(input())
arr = [0]*N
for i in range(N):
    l = []
    temp = input()
    for t in temp:
        l.append(int(t))
    arr[i] = l
matprint(arr)
print()

for i in range(N//2):
    print(N//2)
    for r in range(N//2,-1,-1):
        for j in range(r):
            print('r',r)
            print('몇번 도냐', arr[j][i])
            arr[j][i] = 0
matprint(arr)