
# 시계 방향으로 일치하는지 체크하는 함수
def check(word,pattern,j):
    start = j

    for i in range(1,len(word)):
        if pattern[i] == word[(start+1)%len(word)]:
            start += 1
        else:
            return False
    return True


if __name__ == '__main__':
    N = int(input())
    N_list = [input() for _ in range(N)]

    words = []
    words.append(N_list[0])

    for i in range(1,N):
        pattern = N_list[i]
        flag = 0
        for word in words:
            if len(word) != len(pattern):
                continue

            for j in range(len(word)):
                if pattern[0] == word[j]:
                    if check(word,pattern,j): # 이미 존재하는 애다
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 0:
            words.append(pattern)

    print(len(words))
