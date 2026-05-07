class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        left = 0
        count = {}
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit = fruits[right]
            
            # Add current fruit to basket
            count[fruit] = count.get(fruit, 0) + 1
            
            # If more than 2 types, shrink window
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                
                if count[left_fruit] == 0:
                    del count[left_fruit]
                
                left += 1
            
            # Update maximum window size
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
        