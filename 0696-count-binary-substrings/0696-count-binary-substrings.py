class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        lst=[]
        n=len(s)
        i =0
        while i<n:
            j=i+1
            while j<n and s[i]==s[j]:
                j+=1
            lst.append(j-i)
            i=j
        print(lst)
        res =0
        for i in range(0,len(lst)-1):
            res+=min(lst[i],lst[i+1])
        return res

