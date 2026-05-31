class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        sort_list = sorted(hmap.items(), key = lambda x: -x[1])
        output = []
        for i in range(k):
            output.append(sort_list[i][0])

        return output