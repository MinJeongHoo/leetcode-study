class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
## 2진수로 변환 후 1 카운트