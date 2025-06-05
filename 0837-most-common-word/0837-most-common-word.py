class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        words = paragraph.split(" ")

        word_counts = {}
        for word in words:
            if word and word not in banned:
                word_counts[word] = word_counts.get(word, 0) + 1
        return max(word_counts, key=word_counts.get)