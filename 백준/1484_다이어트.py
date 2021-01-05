if __name__ == '__main__':
    G = int(input())
    s,e=1,2
    flag=0
    while s<e:
        res=(e**2-s**2)
        if res>=G:
            s+=1
            if res==G:
                print(e)
                flag=1
        else:
            e+=1
    if flag==0:
        print(-1)