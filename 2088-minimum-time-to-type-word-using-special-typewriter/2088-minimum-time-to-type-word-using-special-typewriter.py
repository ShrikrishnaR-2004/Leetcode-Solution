class Solution(object):
    def minTimeToType(self, word):
        time = 0
        curr = 'a'

        for c in word:
            diff = abs(ord(curr) - ord(c))

            time += min(diff , 26 - diff)
            time += 1

            curr = c

        return time
        