class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def robLine(arr):
            prev1 = 0  # dp[i-1]
            prev2 = 0  # dp[i-2]

            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            robLine(nums[:-1]),  # exclude last
            robLine(nums[1:])    # exclude first
        )