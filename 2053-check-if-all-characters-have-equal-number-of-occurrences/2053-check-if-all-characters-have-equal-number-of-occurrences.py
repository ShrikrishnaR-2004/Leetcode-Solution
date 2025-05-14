from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        print(count)
        d=count[s[0]]
        for i in count.values():
            if i!=d:
                return False
        return True