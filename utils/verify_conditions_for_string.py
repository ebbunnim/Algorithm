from collections import defaultdict

# expected input
password = "UUUUU"

# play a role like counter
permit_ord_dict = defaultdict(int)

# initial setting
boho=set()
for ele in '~!@#$%^&*':
    boho.add(ord(ele))
ans = [0,0,0,0,0]

# make permit_ord_dict and verify condition4
cnt = 0
curr_str = ''
curr_cnt = 1
flag = 0
for s in password:
    cnt += 1
    permit_ord_dict[s] += 1
    if not flag:
        if curr_str == s:
            curr_cnt += 1
            # 조건 4
            if curr_cnt >= 4:
                ans[3]=1
                flag=1
        else:
            curr_str = s
            curr_cnt = 1

# verify left four conditions
# 조건 1
if cnt < 8 or cnt >= 16:
    ans[0]=1
p1 = p2 = p3 = p4 = 0
for key in permit_ord_dict.keys():
    ord_num=ord(key)
    # 조건 5
    if permit_ord_dict[key] >= 5:
        ans[4]=1
    # 조건 3
    if 48<=ord_num<=57:
        p1=1
    elif 65<=ord_num<=90:
        p2=1
    elif 97<=ord_num<=122:
        p3=1
    elif ord_num in boho:
        p4=1
    # 조건 2
    else:
        ans[1]=1
# 조건 3
if p1+p2+p3+p4<=2:
    ans[2]=1

# got answer
if sum(ans)==0:
    print([0])
else:
    print([idx+1 for idx,val in enumerate(ans) if val==1])


