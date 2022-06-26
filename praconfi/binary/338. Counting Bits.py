class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            result.append(bin(i)[2:])
            
        result = map(lambda x: x.count('1'), result)
        return result
