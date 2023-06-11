class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        sol = 0 
        i = 0
        while True:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1

            buy = prices[i]
            i += 1
            while i < len(prices) and prices[i-1] < prices[i]:
                i += 1 
            i -= 1
            if i == len(prices)-1:
                sol += prices[-1] - buy
                break
            else:
                sol += prices[i] - buy
        return sol