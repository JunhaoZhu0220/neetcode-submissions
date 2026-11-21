class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevTable = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in prevTable:
                prevTable[sorted_string].append(string)
            else:
                prevTable[sorted_string] = [string]
        
        res = []

        for keys in prevTable:
            res.append(prevTable[keys])
        
        return res
        