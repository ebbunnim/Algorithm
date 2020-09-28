from collections import defaultdict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        phones = defaultdict()
        phones['2'] = ['a', 'b', 'c']
        phones['3'] = ['d', 'e', 'f']
        phones['4'] = ['g', 'h', 'i']
        phones['5'] = ['j', 'k', 'l']
        phones['6'] = ['m', 'n', 'o']
        phones['7'] = ['p', 'q', 'r', 's']
        phones['8'] = ['t', 'u', 'v']
        phones['9'] = ['w', 'x', 'y', 'z']
        L = len(digits)

        def dfs(index, res):
            if len(res) == L:
                ans.append(res)
                return

            for i in range(index, len(digits)):
                for alpha in phones[digits[i]]:
                    dfs(i + 1, res+alpha)  # 루트 노드를 다르게 순회해야, res+alpha 전역변수로 설정 주의. 배열이 아니고 문자열이기 때문에 immutable해서 인듯

        if digits == "":
            return []
        dfs(0, '')
        return ans