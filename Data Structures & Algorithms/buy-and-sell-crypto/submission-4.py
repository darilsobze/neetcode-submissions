class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day=0
        sell_day=buy_day+1
        max_profit=0
        while(sell_day<len(prices)):
            if prices[sell_day] >= prices[buy_day]:
                profit= prices[sell_day] - prices[buy_day]
                max_profit = max(profit, max_profit)
                sell_day +=1
            else:
                buy_day = sell_day
                sell_day +=1
        return max_profit
            

            