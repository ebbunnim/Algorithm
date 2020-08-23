import sys
sys.stdin = open("input.txt", "r")

N,M = map(int, input().split())
Data = list(map(int, input().split()))
Q = []
for i in range(N):
    Q.append([Data[i], i])
    #위치를 부여함, 화덕 크기만
print(Q)

i = 0
while len(Q)!=1:
    Q[0][0] //= 2
    if Q[0][0] == 0:
        if N+ i < M:
            Q.pop(0)
            Q.append([Data[N+i], N+i])
            i+=1
        elif N+i >= M:
            Q.pop(0)
    else:
        Q.append(Q.pop(0))

print('#%d' % (Q[0][1]+1))