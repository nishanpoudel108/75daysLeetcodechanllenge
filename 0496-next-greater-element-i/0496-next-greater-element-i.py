class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack = []
        next_greater = {}

        # Find next greater element for every number in nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build answer for nums1
        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result
        