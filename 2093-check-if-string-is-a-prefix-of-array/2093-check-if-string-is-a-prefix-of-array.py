from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        current_concatenation = ""
        
        for word in words:
            current_concatenation += word
            
            if current_concatenation == s:
                return True
            
            if len(current_concatenation) > len(s):
                return False
                
        return False

