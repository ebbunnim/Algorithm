import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    opcode_dic={
        'ADD':'00000',
        'ADDC':'00001',
        'SUB':'00010',
        'SUBC':'00011',
        'MOV':'00100',
        'MOVC':'00101',
        'AND':'00110',
        'ANDC':'00111',
        'OR':'01000',
        'ORC':'01001',
        'NOT':'01010',
        'MULT':'01100',
        'MULTC': '01101',
        'LSFTL':'01110',
        'LSFTLC': '01111',
        'LSFTR':'10000',
        'LSFTRC': '10001',
        'ASFTR':'10010',
        'ASFTRC': '10011',
        'RL':'10100',
        'RLC': '10101',
        'RR':'10110',
        'RRC': '10111',
    }
    for _ in range(N):
        res=''
        opcode,rd,ra,rb_or_c=input().split()
        res+=opcode_dic[opcode]
        res+='0'
        res+=bin(int(rd))[2:].zfill(3)
        res+=bin(int(ra))[2:].zfill(3)
        if res[4]=='0':# rb
            res+=bin(int(rb_or_c))[2:].zfill(3)
            res+='0'
        else:# c#
            res += bin(int(rb_or_c))[2:].zfill(4)
        print(res)

