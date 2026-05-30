class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        s_map = {}
        t_map = {}
        for n in s: 
            s_map[n] = s_map.get(n, 0) + 1
        for n in t:
            t_map[n] = t_map.get(n, 0) + 1
        for val in s_map:
            if val not in t_map:
                return False
            if s_map[val] == t_map[val]:
                continue
            else:
                return False
        return True 


            
            

        