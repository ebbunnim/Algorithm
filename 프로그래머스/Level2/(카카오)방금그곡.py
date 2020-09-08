
def solution(m, musicinfos):
    res = []
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        info[3] = info[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        d1 = info[0].split(':')
        d2 = info[1].split(':')
        delta = (int(d2[0])*60+int(d2[1]))-(int(d1[0])*60+ int(d1[1]))
        s = ''
        for d in range(delta):
            s+=info[3][d%len(info[3])]
        if m in s:
            res.append((delta,info[2]))
    if res == []:
        return "(None)"
    else:
        res.sort(key=lambda x : x[0],reverse=True)
        return res[0][1]
