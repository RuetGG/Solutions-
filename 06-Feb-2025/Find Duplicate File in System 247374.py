# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_content = {}
        for path in paths:
            directory = path.split()
            folder = directory[0]
            for i in range(1, len(directory)):
                start = directory[i].find("(")
                end = directory[i].find(")")
                content = directory[i][start + 1:end + 1]
                file_name = directory[i][:start]
                full_path  = folder + "/" + file_name

                if content not in file_content:
                    file_content[content] = []
                file_content[content].append(full_path)
        return [ans for ans in file_content.values() if len(ans) > 1]