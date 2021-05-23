# 문자열 정렬
def solution(code, day, data):
    info = []
    for d in data:
        p,c,t=d.split(' ')
        if c[5:]==code and t[5:13]==day:
            info.append((t[5:],int(p[6:])))
    info.sort()
    answer = [ele[1] for ele in info]
    return answer