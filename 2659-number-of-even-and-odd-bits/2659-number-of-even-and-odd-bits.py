from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0

        binary = bin(n)[2:]
        
        reversed_binary = binary[::-1]
        
        for i in range(0, len(reversed_binary)):
            if i % 2 != 0 and reversed_binary[i] == "1":
                odd += 1
            
            if i % 2 == 0 and reversed_binary[i] == "1":
                even += 1
        
        l = [even, odd]
        return l

