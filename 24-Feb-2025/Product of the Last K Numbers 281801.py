# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.res = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.res = [1]
        else:
            self.res.append(self.res[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.res):
            return 0
        return self.res[-1] // self.res[-(k + 1)]  
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)