class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevTable = {}
        for i in range(len(nums)):
            if target-nums[i] in prevTable:
                return [prevTable[target-nums[i]], i]
            prevTable[nums[i]] = i
        