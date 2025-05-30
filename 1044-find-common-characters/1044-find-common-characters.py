from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        common_counts = Counter(words[0])

        for i in range(1, len(words)):
            current_word_counts = Counter(words[i])
            common_counts = common_counts & current_word_counts 
            
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)
            
        return result