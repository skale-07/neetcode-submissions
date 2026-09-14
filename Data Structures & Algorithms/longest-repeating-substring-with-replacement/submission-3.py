class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hMap = {}
        longLen = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            hMap[s[r]] = hMap.get(s[r], 0) + 1
            maxf = max(hMap[s[r]], maxf)

            while not (r - l + 1) - maxf <= k:
                hMap[s[l]] = hMap[s[l]] - 1
                l += 1

            longLen = max(longLen, r - l + 1)
        return longLen







