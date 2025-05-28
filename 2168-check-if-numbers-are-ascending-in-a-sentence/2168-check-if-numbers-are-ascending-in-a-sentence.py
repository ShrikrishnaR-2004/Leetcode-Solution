class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_split = s.split(" ")
        digit = []
        for i in s_split:
            if i.isdigit():
                digit.append(int(i))
        
        if not digit:
            return True 
        
        for i in range(1, len(digit)):
            if digit[i] <= digit[i-1]:
                return False
        
        return True
