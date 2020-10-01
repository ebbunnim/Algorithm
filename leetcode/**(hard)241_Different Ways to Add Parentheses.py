class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l) + op + str(r)))
            return res

        if input.isdigit():  # 리턴 조건은 "1개의 숫자"를 만들었을 때. '23'이어도 (!=len(s)이 1) 마지막에 리턴해야 함
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                # divide
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                # conquer
                res.extend(compute(left, right, input[i]))
        return res
