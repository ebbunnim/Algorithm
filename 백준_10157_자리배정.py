import sys
sys.stdin = open("input1.txt", "r")

M, N = map(int, input().split()) #M이 col, N이 row, 이때 range에서 1부터 시작해야
#arr
l = [[0]*N for _ in range(M)] #기본 arr

#행 우선순회 해야
# for i in range(M):
#     for j in range(N,0,-1): #세로가 M이라는 것 주의 (열 우선순회가 맞나?)
#         print((i+1,j))
#         print('이때의 인덱스는', i,6-j)
        # l[i][6-j] = (i+1, j)
        # l[j][i] = (i+1, j)
#         l[i][6-j] = (i,j) #여기서 인덱스도 0부터가 아님?

for col in range(M,-1,-1): #N - 6
    for row in range(N): #M - 7
        # l[row][col] - 행 우선순회
        print((row+1, col+1))


