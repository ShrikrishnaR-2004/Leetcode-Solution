class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiopQWERTYUIOP")
        second_row = set("asdfghjklASDFGHJKL")
        third_row = set("zxcvbnmZXCVBNM")
        result = []
        for word in words:
            first_row_flag = True
            second_row_flag = True
            third_row_flag = True
            for char in word:
                if char not in first_row:
                    first_row_flag = False
                if char not in second_row:
                    second_row_flag = False
                if char not in third_row:
                    third_row_flag = False
            if first_row_flag or second_row_flag or third_row_flag:
                result.append(word)
        return result