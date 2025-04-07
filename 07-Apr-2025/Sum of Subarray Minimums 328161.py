# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        
        prevSmaller = [0] * n
        nextSmaller = [0] * n
        stack = []

        for i in range(n):
            count = 1
            while stack and arr[stack[-1][0]] > arr[i]:
                count += stack.pop()[1]
            prevSmaller[i] = count
            stack.append((i, count))

        stack.clear()

        for i in range(n - 1, -1, -1):
            count = 1
            while stack and arr[stack[-1][0]] >= arr[i]:
                count += stack.pop()[1]
            nextSmaller[i] = count
            stack.append((i, count))

        result = 0
        for i in range(n):
            result += arr[i] * prevSmaller[i] * nextSmaller[i]
            result %= mod

        return result
