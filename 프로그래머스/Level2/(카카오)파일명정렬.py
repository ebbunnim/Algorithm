def solution(files):
    def cut(x):
        head = ''
        for i in range(len(x)):
            if x[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            else:
                head += x[i]
        number = ''
        for j in range(i, len(x)):
            if x[j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            else:
                number += x[j]
        if j != len(x) - 1:
            tail = x[j:]
        else:
            tail = ''
        return [head, number, tail]

    for i in range(len(files)):
        files[i] = cut(files[i])

    for i in range(1, len(files)):
        for j in range(i, 0, -1):
            if files[j][0].upper() < files[j - 1][0].upper():
                files[j], files[j - 1] = files[j - 1], files[j]
            elif files[j][0].upper() == files[j - 1][0].upper():
                if int(files[j][1]) < int(files[j - 1][1]):
                    files[j], files[j - 1] = files[j - 1], files[j]
            else:
                break
    return [''.join(file) for file in files]