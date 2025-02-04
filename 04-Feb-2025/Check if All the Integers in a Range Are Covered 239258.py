# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_set = set()
        for start, end in ranges:
            for num in range(start, end + 1):
                my_set.add(num)
        return all(num in my_set for num in range(left, right + 1))