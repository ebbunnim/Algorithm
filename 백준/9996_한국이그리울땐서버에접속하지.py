if __name__ == '__main__':
    N = int(input())
    pattern = input()
    for i in range(len(pattern)):
        if pattern[i] == '*':
            target = i
            break
    for t in range(N):
        text = input()
        vis = [False]*len(text)
        flag = 0
        for i in range(target): # left
            if vis[i] == False and pattern[i] == text[i]:
                vis[i] = True
            else:
                print('NE')
                flag = 1
                break
        if flag == 0:
            idx = 0
            for i in range(len(pattern)-1,target,-1): # right
                if vis[len(text)-1-idx] == False and pattern[i] == text[len(text)-1-idx]:
                    vis[len(text)-1-idx] = True
                else:
                    print('NE')
                    flag = 1
                    break
                idx += 1
        if flag == 0:
            print('DA')
