from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # split+hash
        tmp = ''
        for p in paragraph:
            if p.isalpha():
                tmp+=p
            else:
                tmp+=' ' # . / , / ' ' 모두 ''로 처리
        tokens = [x.lower() for x in tmp.split() if x.lower() not in banned ]
        counter = Counter(tokens)
        return counter.most_common()[0][0]
        