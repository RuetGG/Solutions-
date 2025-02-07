# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(img[0])
        m = len(img)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum = 0
                count = 0
                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y]
                            count += 1
                            res[i][j] = sum // count
        return res