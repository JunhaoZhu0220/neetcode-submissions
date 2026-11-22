class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minelem = 1001

        while l <= r:
            mid = (l+r)//2
            minelem = min(minelem, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return minelem


        