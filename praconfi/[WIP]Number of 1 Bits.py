class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(n)
        filtered = list(filter(lambda x: x == '1', n))
        return len(filtered)
