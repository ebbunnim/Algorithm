import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    s=input()
    slist=s.split()
    xtype=''
    for i in range(len(slist)):
        if slist[i][-1] not in (',',';'):
            xtype+=slist[i]
            continue
        res=xtype
        reverse_slist=slist[i][:-1][::-1]
        for j in range(len(slist[i])-1):
            if reverse_slist[j]=='[':
                res+=']'
            elif reverse_slist[j]==']':
                res+='['
            elif reverse_slist[j].isalpha():
                break
            else:
                res+=reverse_slist[j]
        word=reverse_slist[j:][::-1]
        res+=' '+word
        res+=';'
        print(res)
