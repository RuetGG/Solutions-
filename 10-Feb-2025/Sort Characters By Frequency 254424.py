# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        s = ""
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        for key, value in sorted_freq:
            s += key * value            
        return s

