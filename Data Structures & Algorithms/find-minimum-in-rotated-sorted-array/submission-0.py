class Solution:
    def findMin(self, nums: List[int]) -> int:
        minelem = nums[0]
        for num in nums:
            minelem = min(minelem, num)
        return minelem
        