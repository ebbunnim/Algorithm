if __name__ == '__main__':

    text = list(input())
    patterns = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    l = len(text)
    cnt = 0
    text_vis = [False]*l
    for i in range(l) : # text
        for z in range(len(patterns)): # pattern 돌아감
            if text_vis[i] == False and text[i] == patterns[z][0]:
                for j in range(1,len(patterns[z])):
                    flag = 0
                    if i+j<l and text[i+j] == patterns[z][j]:
                        pass
                    else:
                        flag = 1
                        break
                if flag == 0:
                    for j in range(0, len(patterns[z])):
                        text_vis[i+j] = True
                    cnt += 1
    for t in text_vis:
        if t == False:
            cnt += 1
    print(cnt)
