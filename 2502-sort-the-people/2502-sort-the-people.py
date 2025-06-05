class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired_data = []
        for i in range(len(names)):
            paired_data.append((heights[i], names[i]))

        paired_data.sort(key=lambda x: x[0], reverse=True)

        sorted_names = [name for height, name in paired_data]

        return sorted_names