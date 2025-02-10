class Solution:
    def clearDigits(self, s: str) -> str:
        str1=[]
        for i in range(len(s)):
            if not s[i].isdigit():
                str1.append(s[i])
            else:
                str1.pop()
        return "".join(str1)
            