import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_words = re.sub(r'[^a-zA-Z0-9]', ' ', paragraph).lower().split()
        banned_set = set(banned)
        
        word_counts = Counter()
        for word in normalized_words:
            if word and word not in banned_set:
                word_counts[word] += 1
        
        if word_counts:
            return word_counts.most_common(1)[0][0]
        else:
            return ""