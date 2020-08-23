if __name__ == '__main__':
    input_v = list(map(int, input()))
    if 0 not in input_v:
        print(-1)
    elif sum(input_v)%3 != 0:
        print(-1)
    else:
        input_v.sort(reverse=True)
        for v in input_v:
            print(v, end='')
