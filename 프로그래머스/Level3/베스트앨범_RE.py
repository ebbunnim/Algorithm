from collections import defaultdict


def solution(genres, plays):
    # 장르별 누적된 재생 수 많을 수록
    mydict = defaultdict(int)
    for i in range(len(genres)):
        mydict[genres[i]] += plays[i]
    sort_by_songs = sorted(mydict, key=lambda x: mydict[x], reverse=True)

    # 장르 내에서 가장 많이 재생된 노래 (인덱스), 같다면 인덱스 번호 오름차순
    songs_dict = defaultdict(list)
    for idx, val in enumerate(plays):
        songs_dict[genres[idx]] += [(idx, val)]
    for key in songs_dict:
        songs_dict[key].sort(key=lambda x: (x[1], -x[0]), reverse=True)
    res = []
    for genre in sort_by_songs:  # 누적수대로 순차적으로
        if len(songs_dict[genre]) == 1:
            res += [songs_dict[genre][0]]
        else:
            res += [songs_dict[genre][0]]
            res += [songs_dict[genre][1]]
    return [r[0] for r in res]