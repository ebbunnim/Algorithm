
if __name__ == '__main__':
    input_v = input()
    values = []
    start = 0
    for i in range(len(input_v)):
        if input_v[i] == '-' or input_v[i] == '+':
            values.append(int(input_v[start: i]))
            values.append(input_v[i])
            start = i+1
    values.append(int(input_v[start:]))

    cal = 0
    flag = False
    for i in range(len(values)):
        if values[i] == '-':
            flag = True
            continue # 수치 처리 안해야 하므로
        elif values[i] == '+':
            continue

        if flag == True:
            cal -=  values[i]
        else:
            cal += values[i]
    print(cal)