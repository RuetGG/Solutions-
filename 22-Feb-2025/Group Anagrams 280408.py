# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            word[key].append(s)
        return list(word.values())