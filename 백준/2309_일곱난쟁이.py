if __name__ == '__main__':
    L = [int(input()) for _ in range(9)]
    L.sort()
    sum_v = sum(L)
    for i in range(9):
        for j in range(i+1,9):
            if sum_v - L[i] - L[j] == 100:
                for a in range(9):
                    if a == i or a == j:
                        continue
                    else:
                        print(L[a])
                exit()