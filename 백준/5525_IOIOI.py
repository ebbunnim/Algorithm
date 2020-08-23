if __name__ == '__main__':
    N = int(input())
    pattern = ''
    cnt = 0
    S = int(input())
    text = input()

    D = [0]*S

    for i in range(2, S):
        if text[i] == 'I': #back:
            if text[i-1] == 'O' and text[i-2] == 'I':
                D[i] = D[i-2]+1


    for i in range(S):

        if N <= D[i] :
            cnt += 1
    print(cnt)