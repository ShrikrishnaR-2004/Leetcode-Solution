class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        start_index = 0

        if s[0] == '-':
            sign = -1
            start_index = 1
        elif s[0] == '+':
            start_index = 1

        result = 0
        for i in range(start_index, len(s)):
            if s[i].isdigit():
                digit = int(s[i])

                # Corrected overflow checks
                if result > 214748364 or (result == 214748364 and digit > 7):
                    if sign == 1:
                        return 2147483647
                    else:
                        return -2147483648

                result = result * 10 + digit
            else:
                break

        return result * sign