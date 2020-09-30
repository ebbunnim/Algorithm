class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1') # 눌린채 남아있는 자리수가 있다면, 그게 다른 숫자 혹은 문자라는 의미