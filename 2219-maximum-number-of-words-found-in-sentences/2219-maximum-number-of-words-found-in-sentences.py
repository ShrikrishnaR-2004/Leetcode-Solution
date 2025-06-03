class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for i in range(len(sentences)):
            res=max(res,len(sentences[i].split()))
        return res