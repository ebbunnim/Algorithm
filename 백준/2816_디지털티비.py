if __name__ == '__main__':
    N = int(input())
    N_list = [input() for _ in range(N)]
    for i in range(N):
        if N_list[i] == 'KBS1':
            idx1 = i
        elif N_list[i] == 'KBS2':
            idx2 = i


    # 무조건 idx1을 먼저 스왑하며 위치시켜야 하므로, 앞에 있던 idx2는 밀려나게 되어있다.
    if idx1 > idx2:
        idx2 += 1

    print('1'*idx1 + '4'*idx1 + '1'*idx2 + '4'*(idx2-1))