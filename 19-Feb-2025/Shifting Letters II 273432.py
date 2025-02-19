# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for st, en, direct in shifts:
            if direct == 0:
                arr[st] -= 1
                arr[en + 1] += 1 
            else:
                arr[st] += 1
                arr[en + 1] -= 1
        acc = 0 
        pre = []
        for i in arr:
            acc += i
            pre.append(acc)
 
        ans = []
        for i in range(len(s)):
            res = ord(s[i]) - 97
            res += pre[i]
            res %= 26
            res += 97
            ans.append(chr(res))
        return ''.join(ans)