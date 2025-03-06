from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                l.append(grid[i][j])
        
        counter = Counter(l)
        repeated = 0
        for key, value in counter.items():
            if value > 1:
                repeated = key
                break
        
        expected_sum = (n * n * (n * n + 1)) // 2
        actual_sum = sum(l)
        
        missing = expected_sum - (actual_sum - repeated)
        
        return [repeated, missing]