class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        output = []

        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word not in anagrams:
                anagrams[sort_word] = [word]
            else:
                anagrams[sort_word].append(word)

        return list(anagrams.values())