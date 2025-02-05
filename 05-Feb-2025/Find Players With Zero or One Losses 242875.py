# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        my_dict = Counter(match[1] for match in matches)
        my_set = set(match[0] for match in matches)

        for i in my_set:
            if i not in my_dict:
                ans[0].append(i)
        for j, count in my_dict.items():
            if count == 1:
                ans[1].append(j)

        ans[0].sort()
        ans[1].sort()
        return ans  