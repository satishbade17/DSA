class Solution:
    def findPow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        half = self.findPow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x