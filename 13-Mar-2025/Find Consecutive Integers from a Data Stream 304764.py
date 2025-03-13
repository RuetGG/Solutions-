# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value 
        self.k = k
        self.queue = deque()    
        self.count = 0


    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        self.queue.append(num)
        if num == self.value:
            self.count += 1

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            if removed == self.value:
                self.count -= 1
        
        return self.count == self.k