# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = []
        l = 0
        while l < len(s):
            i = l
            maxi = s.rfind(s[l])
            while l < maxi:
                l += 1
                if len(s) > l and maxi < s.rfind(s[l]):
                    maxi = s.rfind(s[l])
            arr.append(l - i + 1)
            l += 1
        return arr