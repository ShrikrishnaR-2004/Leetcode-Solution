class Solution:
    def isValid(self, s: str) -> bool:
        x={"]":"[","}":"{",")":"("}
        st=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            else:
                if not st or x[i] != st.pop():
                    return False
        return len(st)==0 
        