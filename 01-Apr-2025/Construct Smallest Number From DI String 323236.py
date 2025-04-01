# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        count = 1
        stack = []
        temp = []
        for p in pattern:
            if p == "D":
                temp.append(count)

            else:
                temp.append(count)
                while temp:
                    val = temp.pop()
                    stack.append(val)
            count += 1
        temp.append(count)
        while temp:
            val = temp.pop()
            stack.append(val)

        return ''.join(map(str, stack))
                
