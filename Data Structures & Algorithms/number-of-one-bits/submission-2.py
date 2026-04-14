class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        halves = 1
        while n > 2:
            if n % 2 != 0:
                n = n - 1
                halves += 1
            n = n / 2
        return halves