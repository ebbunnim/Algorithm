import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(T):
        n = int(sys.stdin.readline())
        input_list = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
        cnt = 0
        input_list.sort(key=lambda x : x[0])

        for i in range(n):
            if i == 0:
                min = input_list[i][1]
                cnt+=1
                continue

            if input_list[i][1] < min:
                cnt += 1
                min = input_list[i][1]

        print(cnt)