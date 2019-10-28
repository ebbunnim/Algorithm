import sys
sys.stdin = open("4875.txt", "r")

def is_ok(x,y):
    return 0<=x<N and 0<=y< N and mymap[x][y] != 1

def find_map(start_X, start_Y): #출발해서 3을 만나면 끝
    global result #이게 있었어야

    if mymap[start_X][start_Y] == 3:
        result = 1
        return

    if is_ok(start_X-1, start_Y) and (start_X-1,start_Y) not in visited:
        visited.append((start_X-1, start_Y))
        find_map(start_X-1, start_Y)
    if is_ok(start_X+1, start_Y) and (start_X+1,start_Y) not in visited:
        visited.append((start_X+1, start_Y))
        find_map(start_X+1, start_Y)
    if is_ok(start_X, start_Y-1) and (start_X,start_Y-1) not in visited:
        visited.append((start_X, start_Y-1))
        find_map(start_X, start_Y-1)
    if is_ok(start_X, start_Y+1) and (start_X,start_Y+1) not in visited:
        visited.append((start_X, start_Y+1))
        find_map(start_X, start_Y+1)


if __name__=='__main__':
    T = int(input())
    for tc in range(1,T+1):
        N = int(input())
        mymap = [0]*N
        for k in range(N):
            temp = input()
            l = [0]*N
            for i in range(len(temp)):
                l[i] = int(temp[i])
            mymap[k] = l
        print(mymap)
        for i in range(N):
            for j in range(N):
                if mymap[i][j] == 2:
                    start_X = i
                    start_Y = j
        print(start_X, start_Y)
        visited = []
        visited.append((start_X, start_Y))
        result=0
        find_map(start_X, start_Y)
        print('#%d %d' % (tc,result))


