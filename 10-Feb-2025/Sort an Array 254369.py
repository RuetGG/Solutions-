# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        mini = min(nums)
        offset = -mini
        count = [0] * (maxi + 1 - mini)
        for i in nums:
            count[i + offset] += 1
            print(i + offset)

        ans = []
        for index in range(len(count)):
            for _ in range(count[index]):
                ans.append(index - offset)
        return ans
        