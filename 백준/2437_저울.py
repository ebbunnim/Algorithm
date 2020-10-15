import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().split(' ')))
    n_list.sort()
    acc = 0
    for i in range(n):
        if acc+1 < n_list[i]:
            # print(acc+1) # 여기에 출력하면 안됨.(반례) 1 입력 1 출력
            break
        acc+=n_list[i]

    print(acc + 1)
