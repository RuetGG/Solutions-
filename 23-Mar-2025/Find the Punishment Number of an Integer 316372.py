# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = [1]

        def split(index, ans, target, curr_sum):
            if index == len(ans):
                if curr_sum == target:
                    res.append(int(ans))
                    return True
                return False

            for i in range(index + 1, len(ans) + 1):
                part = int(ans[index:i])
                if split(i, ans, target, curr_sum + part):
                    return True
            return False
               

        for i in range(2, n + 1):
            ans = i * i
            split(0, str(ans), i, 0)

        return sum(res)