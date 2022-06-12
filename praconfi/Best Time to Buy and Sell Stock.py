# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# https://leetcode.com/submissions/detail/720060659/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 아무리 큰 금액이어도 갱신되게 하기위해 os의 가장 큰값으로 초기화함
        buy_price = sys.maxsize
        profit = 0
        
        # 최대가격과 최소가격을 갱신
        for price in prices:
            buy_price = min(price, buy_price)
            profit = max(profit, price - buy_price)
        return profit