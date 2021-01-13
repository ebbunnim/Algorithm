def is_same_or_prior(a, b):
    if b in {'+','-'} and a in {'*','/','-','+'}:
        return True
    if b in {'*','/'} and a in  {'*','/'}:
        return True
    return False

if __name__ == '__main__':
    strings=input()
    stack=[]
    ans=''
    for s in strings:
        if s.isalpha():
            ans+=s
            continue

        if s=='(':
            stack.append(s)
        elif s==')':
            while stack and stack[-1]!='(':
                ans+=stack.pop()
            stack.pop()
        else: # +,-,/,*
            while stack and is_same_or_prior(stack[-1],s):
                ans+=stack.pop()
            stack.append(s)

    while stack:
        ans+=stack.pop()
    print(ans)
