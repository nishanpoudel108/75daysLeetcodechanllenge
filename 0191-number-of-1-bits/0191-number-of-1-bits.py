class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n:
            count += n & 1  # Check if the last bit is 1
            n >>= 1         # Shift right by 1 bit

        return count