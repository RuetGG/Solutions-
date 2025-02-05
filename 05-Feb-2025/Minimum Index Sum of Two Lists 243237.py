# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1Dict = {}
        mini = len(list1) + len(list2)
        result = []
        for i in range(len(list1)):
            list1Dict[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in list1Dict:
                index_sum = list1Dict[list2[i]] + i 
                if index_sum < mini:
                    mini = index_sum 
                    result = [list2[i]] 
                elif index_sum == mini:
                    result.append(list2[i])  
        return result