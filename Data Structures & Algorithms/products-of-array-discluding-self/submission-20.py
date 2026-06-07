class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                product[i] *= prefix
            else:
                prefix = prefix * nums[i-1]
                product[i] *= prefix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                product[i] *= postfix
            else:
                postfix = postfix * nums[i+1]
                product[i] *= postfix 
        
        return product
