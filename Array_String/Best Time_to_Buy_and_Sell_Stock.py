class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1 
        maxs = 0 

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxs = max(maxs, profit)
            else:
                left = right
            right += 1
        return(maxs)
