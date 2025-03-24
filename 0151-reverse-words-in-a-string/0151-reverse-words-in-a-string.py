class Solution:
    def reverseWords(self, s: str) -> str:
        rev_words=s.split()
        res=[]

        for i in range(len(rev_words)-1,-1,-1):
            res.append(rev_words[i])
            if i!=0:
                res.append(" ")
        return "".join(res)
