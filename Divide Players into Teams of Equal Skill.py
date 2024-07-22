class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        res = []
        skill.sort()
        left, right = 0, len(skill) - 1 
        target = skill[left] + skill[right]
        prod = 0
        while left < right:
            if skill[left] + skill[right] == target:
                prod += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return prod 
