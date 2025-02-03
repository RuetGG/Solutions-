# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myS_dict = {}
        myT_dict = {}
        for char in t:
            if char not in myT_dict:
                myT_dict[char] = 1
            else:
                myT_dict[char] += 1

        for char in s:
            if char not in myS_dict:
                myS_dict[char] = 1
            else:
                myS_dict[char] += 1
        return myT_dict == myS_dict