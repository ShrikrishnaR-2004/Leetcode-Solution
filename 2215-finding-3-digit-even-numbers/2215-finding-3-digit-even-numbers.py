from collections import Counter
from typing import List
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        even_numbers = []
        digit_counts = Counter(digits)

        for i in range(100, 1000, 2):
            s_num = str(i)
            num_counts = Counter(map(int, s_num))
            Flag = True
            for digit, count in num_counts.items():
                if digit_counts[digit] < count:
                    Flag = False
                    break
            if Flag:
                even_numbers.append(i)

        return sorted(even_numbers)