## 가장 최소한의 수를 구한 다음 가장 큰 수를 빼주면 된다.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum = prices[0]
        result = 0
        for i in range(1,len(prices)):
            if minNum>prices[i]:
                minNum = prices[i]
            benefit = minNum-prices[i]
            if benefit<0 and benefit<result:
                result = benefit
        return abs(result)
