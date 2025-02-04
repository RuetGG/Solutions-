# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        res = ""
        if "@" in s:
            s = s.lower()
            index = s.index("@")
            res = s[0] + "*****" + s[index - 1:] 
        else:
            if any(char.isdigit() for char in s):
                ans = []
                for char in s:
                    if char.isdigit():
                        ans.append(int(char))
                left = 0
                diff = len(ans)- 10
                if diff == 0:
                    res = "***-***-" + "".join(map(str, ans[6:]))
                elif diff == 1:
                    res =  "+*-***-***-" + "".join(map(str,ans[7:]))
                elif diff == 2:
                    res = "+**-***-***-" + "".join(map(str,ans[8:]))
                elif diff == 3:
                    res = "+***-***-***-" + "".join(map(str,ans[9:]))
        return res               