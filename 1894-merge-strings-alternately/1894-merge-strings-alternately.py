class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        lon=max(len(word1),len(word2))
        for i in range(lon):
            if i<len(word1):
                s+=word1[i]
            if i<len(word2):
                s+=word2[i]
        return s