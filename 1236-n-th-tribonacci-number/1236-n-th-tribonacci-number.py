class Solution:
    def tribonacci(self, n: int) -> int:
        if (n == 0 ) :
            return 0
        if (n == 1 or n ==2) :
            return 1
        first,second,third=0,1,1
        for i in range(3,n+1):
            cur=first+second+third
            first=second
            second=third
            third=cur
        return third        