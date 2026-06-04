# week 15-3a.py 學習計劃 DP-Multidimention 第三題
# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, can_buy):
            if i == len(prices):
                return 0
            if can_buy:
                return max(dp(i+1, True), dp(i+1, False) - prices[i])
            else:
                return max(dp(i+1, False), dp(i+1, True) + prices[i] - fee)
        return dp(0, True)
# week 15-3b.py 學習計劃 DP-Multidimention 第三題
# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0
        for price in prices[1:]:
            sell = max(sell, price + buy - fee)
            buy = max(buy, sell - price)
        return sell