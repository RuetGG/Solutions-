# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        response = {}
        ans = 0
        for answer in answers:
            response[answer] = response.get(answer, 0) + 1

        for key, value in response.items():
            group = key + 1
            ans += ((value + group - 1) // group) * group
        return ans 