class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        profit = 0

        for r in range(len(prices)):
            currProf = prices[r] - prices[l]
            if profit > currProf:
                if prices[r] < prices[l]:
                    l = r
            profit = max(currProf, profit)
        return profit    




