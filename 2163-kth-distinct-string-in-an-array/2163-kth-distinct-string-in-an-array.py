from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        no_freq=Counter(arr)
        print(no_freq)
        l=[]
        for i,j in no_freq.items():
            if j==1:
                l.append(i)

        if k>0 and k<=len(l):
            return l[k-1]
        else:
            return ""