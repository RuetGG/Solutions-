# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = 1
        ans = 0
        pre = 0
        for num in nums:
            pre += num
            if pre - goal in my_dict:
                ans += my_dict[pre - goal]
            my_dict[pre] += 1
        return ans