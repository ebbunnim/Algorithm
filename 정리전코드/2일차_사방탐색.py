
def my_abs(a, b):
    if a > b : return a-b
    else : return b-a


def iswall(a):
    if a < 0 or a >= 5 : return True
    else : return False




arr=[[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
sum_result=0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for I in range(4): #사방탐색

            if iswall(i+dx[I]) + iswall(j+dy[I]) == False:

                result = my_abs(arr[i][j], arr[i+dx[I]][j+dy[I]])
                sum_result += result

print(sum_result)





