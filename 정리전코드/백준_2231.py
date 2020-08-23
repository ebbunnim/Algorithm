import sys
sys.stdin = open("input.txt", "r")

N = int(input())
# N을 만드는 생성자 중 가장 작은 애
ans = 9999999
for i in range(N):
    nn = len(str(i))
    res=0
    for j in range(nn):
        res+=int(str(i)[j])
    i+=res

    if i == N:
        if i-res < ans:
            ans = i-res
if ans == 9999999:
    print(0)
else:
    print(ans)
