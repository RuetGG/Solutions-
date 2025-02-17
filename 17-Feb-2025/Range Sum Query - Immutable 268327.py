# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.arr.append(curr_sum)
        
    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.arr[right]
        if left > 0:
            left_sum = self.arr[left - 1]
        else:
            left_sum = 0
        return right_sum - left_sum 

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)