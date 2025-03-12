# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findString(n):
            if n == 1:
                return "0"
            prev = findString(n - 1)
            return prev + "1" + reverseString(invert(prev))

        def reverseString(bits):
            return ''.join(reversed(bits))

        def invert(bits):

            return ''.join('1' if bit == "0" else "0" for bit in bits)

        ans = findString(n)
        print(ans)

        return ans[k - 1]