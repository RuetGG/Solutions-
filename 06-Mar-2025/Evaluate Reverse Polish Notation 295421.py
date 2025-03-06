# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in  operations:
                stack.append(int(token))

            else:
                val1 = stack.pop()
                val2 = stack.pop()
                        
                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                else:
                    stack.append(int(val2 / val1))
                
        return stack[0] 