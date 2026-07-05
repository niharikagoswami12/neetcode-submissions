class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_v=0
        min_v=float('inf')
        for i in range(len(prices)):
            if prices[i]<min_v:
                min_v=prices[i]
            if max_v<prices[i]-min_v:
                max_v=prices[i]-min_v
        return max_v
        