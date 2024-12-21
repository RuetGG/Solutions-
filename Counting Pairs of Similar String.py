class Solution:
    def similarPairs(self, words: List[str]) -> int:

        i = 0
        count = 0

        while i < len(words):
            j = i + 1
            while j < len(words):
                if set(words[i]) == set(words[j]):
                    count += 1
                j += 1
            i += 1
        return count
