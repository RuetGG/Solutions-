class Solution:
    def reverseVowels(self, s: str) -> str:
        my_dict = {"a","e", "i" ,"o", "u", "A", "E", "I", "O", "U"}
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in my_dict:
                left += 1
            else:
                if s[right] not in my_dict:
                    right -= 1
                else: 
                    s[left], s[right] = s[right] , s[left]
                    left += 1
                    right -= 1
        return ''.join(s)
