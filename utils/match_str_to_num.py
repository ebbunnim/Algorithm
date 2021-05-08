import re

def solution(s):
    n=len(s)
    D={
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }
    def match(c):
        if c=='ze':
            return '0',4
        elif c=='on':
            return '1',3
        elif c=='tw':
            return '2',3
        elif c=='th':
            return '3',5
        elif c=='fo':
            return '4',4
        elif c=='fi':
            return '5',4
        elif c=='si':
            return '6',3
        elif c=='se':
            return '7',5
        elif c=='ei':
            return '8',5
        else:
            return '9',4
    l,r=0,0
    ans=''
    while r<n:
        if s[r].isdigit():
            ans+=s[r]
            r+=1
        else:
            ele,length=match(s[r:r+2])
            ans+=ele
            r+=length
    return int(ans)