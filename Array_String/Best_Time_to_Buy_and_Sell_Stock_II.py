class Solution(object):
    def maxProfit(self, prices):
        otv=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                otv+=prices[i]-prices[i-1]
        return otv
#просто проверяем больше ли сегодня акции чем вчера, ведь мы можем продать акцию и сразу же купить её снова в один и тот же день
# 2ms 13.7 mb
