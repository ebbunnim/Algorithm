def solution(w,h):
    def gcd(w, h):
        while h!=0:
            w, h = h, w%h
        return w
    x = gcd(w,h)
    if x == 1:
        return w*h-(w+h-1)
    else:
        return w*h-(x*(w//x+h//x-1))
