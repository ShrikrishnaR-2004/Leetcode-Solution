class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        strs.sort()
        i=0
        if n==0:
            return ""
        if n==1:
            return strs[0]
        minlen=min(len(strs[0]),len(strs[n-1]))
        while i<minlen and strs[0][i]==strs[n-1][i]:
            i+=1
        common=strs[0][0:i]
        return common