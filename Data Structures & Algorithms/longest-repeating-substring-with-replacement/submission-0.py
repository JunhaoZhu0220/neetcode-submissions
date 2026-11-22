class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charTable = {}
        l = 0
        maxLength = 0

        for r in range(len(s)):
            charTable[s[r]] = charTable.get(s[r], 0) + 1

            # Find the most frequent element in the hashmap
            max_freq = max(charTable.values())
            while r-l+1 > max_freq + k:
                charTable[s[l]] = charTable.get(s[l]) - 1
                l += 1
            
            maxLength = max(maxLength, r-l+1)
        
        return maxLength
