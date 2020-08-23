import sys
sys.stdin = open("input.txt","r")

T=10

for tc in range(1, T+1):


    def iswall(start_row, start_col): #list index out of range를 제어할 조건ans
        search_idx = [(0, -1),(0, 1),(-1, 0)]
        if start_col - 1 < 0:
            search_idx = [(0,0),(0,1),(-1,0)] # 좌,우,상(얘만 row)
        elif start_col + 1 > 99:
            search_idx = [(0,-1),(0,0),(-1,0)]
        elif start_row - 1 < 0:
            search_idx = [(0, -1), (0, 1), (0, 0)]
        return search_idx


    def direction(start_row, start_col): #기본은 위로, 아니라면 1을 찾아 좌,우로. 위로보다 좌,우가 우선함.
        while start_row > 0:
            print(start_row,start_col)
            search_idx = iswall(start_row, start_col)
            print(search_idx)
            if l[start_row][start_col + search_idx[0][1]] == 1:
                start_col -= 1
                l[start_row][start_col]=0
            elif l[start_row][start_col + search_idx[1][1]] == 1:
                start_col += 1
                l[start_row][start_col] = 0
            elif l[start_row + search_idx[2][0]][start_col] == 1:
                start_row -= 1
                l[start_row][start_col] = 0  # 순서에 주의! 움직이고 난 위치를 0으로 만들어줘야! iswall에서 ==1에 잡힘
                if start_row == 0:
                    return start_col
                    break
        return start_col #default 어떻게 설정해야?


    if __name__ == '__main__':
        t = int(input())
        l = [list(map(int, input().split())) for _ in range(100)]
        # 모두 인덱스가 기본임
        start_row, start_col = 99, l[99].index(2)
        target = direction(start_row, start_col)
        print('#%d %d' % (tc,target))



