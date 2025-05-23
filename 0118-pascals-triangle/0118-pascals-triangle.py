class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        lst = []
        for i in range(numRows):
            row = [1]  
            if i > 0:
                prev_row = lst[i - 1]
                for j in range(i - 1):
                    row.append(prev_row[j] + prev_row[j + 1])
                row.append(1) 
            lst.append(row)
        return lst