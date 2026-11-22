class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        l, r = 0, 1

        while l <= len(prices)-1 and r <= len(prices)-1:
            max_pro = max(max_pro, prices[r]-prices[l])

            if prices[l] > prices[r]:
                l = r
            
            r += 1
        
        return max_pro
