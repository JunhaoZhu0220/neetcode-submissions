class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}

        for string in s:
            time = s_table.get(string, 0) + 1
            s_table[string] = time

        for string in t:
            time = t_table.get(string, 0) + 1
            t_table[string] = time

        if s_table == t_table:
            return True
        
        return False
        