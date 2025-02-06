# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        ansCount = Counter(chars)
        for word in words:
            wordCount = Counter(word)
            if all(wordCount[char] <= ansCount[char] for char in wordCount):
                ans += len(word)
        return ans 