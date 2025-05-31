class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            binary=(bin(i)[2:])
            count=0
            for one in binary:
                if one == "1":
                    count+=1
            l.append(count)
        return l
