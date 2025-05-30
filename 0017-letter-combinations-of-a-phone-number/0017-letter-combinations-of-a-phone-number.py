from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""] if digits else []

        if not digits:
            return []

        for char_digit in digits:
            current_letters = letter[char_digit]
            print(current_letters)
            new_combinations = []
            for combination in res:
                for letter_char in current_letters:
                    new_combinations.append(combination + letter_char)
            res = new_combinations

        return res
