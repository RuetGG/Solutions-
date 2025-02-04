# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        res = []
        while k > 0:
            k -= 1
            max_key = max(my_dict, key = my_dict.get)
            res.append(max_key)
            del my_dict[max_key]
        return res