class Solution:
    def freqAlphabets(self, s: str) -> str:
        parts = []
        i = 0
        while i < len(s):
            if  i + 2 < len(s) and s[i+2] == "#":
                parts.append(s[i:i+2])
                i += 3
            else:
                parts.append(s[i])
                i += 1
        result = ""
        for char in parts:
            if char[-1] == "#":
                num = int(part[:-1])
                result += chr(num + 96)

            else:
                num = int(char)
                result += chr(num + 96)
        return result
