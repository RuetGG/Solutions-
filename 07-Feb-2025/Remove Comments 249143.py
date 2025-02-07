# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans, buffer, isOpen = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                if i < len(line) - 1 and line[i] == '/' and line[i+1] =='/' and not isOpen:
                    break
                elif i < len(line) - 1 and line[i] == '/' and line[i+1] == '*' and not isOpen:
                    isOpen = True
                    i += 1
                elif i < len(line) - 1 and line[i] == '*' and line[i+1] == '/' and isOpen:
                    isOpen = False
                    i += 1
                elif not isOpen:
                    buffer += line[i]
                i += 1
            if buffer and not isOpen:
                ans.append(buffer)
                buffer = ''

        return ans     