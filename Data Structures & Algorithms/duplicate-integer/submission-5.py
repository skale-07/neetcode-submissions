class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        initial_set = set(nums)
        if len(initial_set) < len(nums):
            return True
        else:
            return False
