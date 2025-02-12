class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisor_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:
                    divisor_sum += num // i
        
        return divisor_sum == num

        # if num%2==1:
        #     return False
        
        # sum1=0
        # for i in range(1,num//2+1):
        #     if num%i==0:
        #         sum1+=i
        # return sum1==num