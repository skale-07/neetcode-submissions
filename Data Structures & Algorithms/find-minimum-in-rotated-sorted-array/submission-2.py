class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            if l < len(nums) - 1 and nums[l] > nums[l+1]:
                pivot = l + 1
                break
            elif r > 0 and nums[r] < nums[r-1]:
                pivot = r
                break
            r -= 1
            l += 1
        
        return nums[pivot]