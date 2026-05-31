class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, val in enumerate(nums):
            temp_list = nums
            temp_list[i] = -2
            if target - val in temp_list:
                return sorted([i, temp_list.index(target-val)])
