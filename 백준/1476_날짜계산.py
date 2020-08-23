if __name__ == '__main__':
    E, S, M = map(int, input().split())
    year = 1
    while True:
        if (year-E)%15 == 0 and (year-S)%28 == 0 and (year-M)%19 == 0:
            print(year)
            break
        else:
            year += 1
