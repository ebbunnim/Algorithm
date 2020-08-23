if __name__ == '__main__':
    n = int(input())
    n_list = [0] * n
    for i in range(n):
        n_list[i] = int(input())

    n_list.sort()
    max_v = 0
    for i in range(n):
        if n_list[i] * (n - i) >= max_v:
            max_v = n_list[i] * (n - i)
    print(max_v)