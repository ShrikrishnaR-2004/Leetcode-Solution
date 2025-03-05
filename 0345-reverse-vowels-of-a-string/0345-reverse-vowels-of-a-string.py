class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        for i in s:
            if i in "AaEeIiOoUu":
                l.append(i)
        l.reverse()  
        
        result = list(s) 
        print(result)
        vowel_index = 0
        for i in range(len(result)):
            if result[i] in "AaEeIiOoUu":
                result[i] = l[vowel_index]
                vowel_index += 1
        
        return "".join(result) 