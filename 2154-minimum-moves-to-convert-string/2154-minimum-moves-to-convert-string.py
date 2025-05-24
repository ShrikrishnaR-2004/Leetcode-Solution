class Solution:
    def minimumMoves(self, s: str) -> int:
        move=0
        i=0
        n=len(s)
        while i<n:
            if s[i]=="X":
                move+=1
                i+=3
            else:
                i+=1
        return move