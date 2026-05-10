class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        stack = []   # stores indices
        max_area = 0
        
        # Add an extra 0 height to process remaining bars
        heights.append(0)
        
        for i in range(len(heights)):
            
            # If current bar is smaller, calculate area
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                # Width calculation
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                
                max_area = max(max_area, h * w)
            
            stack.append(i)
        
        return max_area
        