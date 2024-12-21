class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        count = 0 
        people.sort()
        while len(people) > 1:
            if  people[0] + people[len(people) - 1] <= limit:
                count += 1
                people.pop(-1)
                people.pop(0)
            else:
                count += 1
                people.pop(-1)

        if len(people) == 1 and people[0] <= limit:
            count += 1

        return count
