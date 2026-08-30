class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}

        for string in strs:
            tempSort = tuple(sorted(string))
            if tempSort in hMap:
                hMap[tempSort].append(string)
            else:
                hMap[tempSort] = [string]
        
        return list(hMap.values())
