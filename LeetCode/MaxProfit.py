class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_sofar = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < lowest_sofar:
                lowest_sofar = prices[i]
            profit_today = prices[i] - lowest_sofar
            max_profit = max(max_profit, profit_today)
        return max_profit
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

