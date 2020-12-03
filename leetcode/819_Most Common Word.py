from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [x for x in re.sub('[^\w]',' ',paragraph).lower().split() if x not in banned]
        return Counter(words).most_common()[0][0]
    

        # 이전풀이
        # tmp = ''
        # for p in paragraph:
        #     if p.isalpha():
        #         tmp+=p
        #     else:
        #         tmp+=' ' # . / , / ' ' 모두 ''로 처리
        # tokens = [x.lower() for x in tmp.split() if x.lower() not in banned ]
        # counter = Counter(tokens)
        # return counter.most_common()[0][0]
        