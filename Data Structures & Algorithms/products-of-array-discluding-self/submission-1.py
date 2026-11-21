class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPro = [1] * (len(nums))
        postfixPro = [1] * (len(nums))
        # [1,1,1,1]

        res = []
        
        for i in range(1, len(nums)):
            prefixPro[i] = prefixPro[i-1]*nums[i-1]

        # [1,2,4,6] => [1,1,2,8]
        
        for j in range(len(nums)-2,-1,-1):
            postfixPro[j] = postfixPro[j+1]*nums[j+1]
        
        # [1,2,4,6] => [48,24,6,1]
        
        for m in range(len(nums)):
            res.append(prefixPro[m]*postfixPro[m])
        
        return res