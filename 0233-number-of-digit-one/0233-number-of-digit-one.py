class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        
        ones = 0
        m = 1

        while m <= n:
            a = n // (m * 10)
            b = n % (m * 10)
            
            ones += a * m
            
            digit = b // m
            
            if digit == 1:
                ones += (b % m) + 1
            elif digit > 1:
                ones += m
            
            m *= 10
            
        return ones