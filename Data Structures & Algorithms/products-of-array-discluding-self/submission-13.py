class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        
        for i, num in enumerate(nums):
            temp_list = nums[:]
            temp_list[i] = None 
            for n in temp_list:
                if n == None:
                    continue
                else:
                    product[i] = product[i] * n
        return product