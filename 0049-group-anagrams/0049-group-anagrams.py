from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagram=defaultdict(list)
        for ch in strs:
            key="".join(sorted(ch.lower()))

            map_anagram[key].append(ch)

        return list(map_anagram.values())