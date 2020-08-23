
def bomb():
    for i in range(len(text)):
        stack.append(text[i])

        if pattern[-1] == text[i]:
            if stack[len(stack)-L:len(stack)] == list(pattern):
                for j in range(L):
                    stack.pop()
    return


if __name__ == '__main__':
    text = input()
    pattern = input()
    L = len(pattern)

    stack = []

    bomb()
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')
