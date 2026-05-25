class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        
        freq = Counter(tasks)
        
        # Maximum frequency of any task
        max_freq = max(freq.values())
        
        # Count how many tasks have the maximum frequency
        max_count = list(freq.values()).count(max_freq)
        
        # Minimum intervals required based on arrangement formula
        intervals = (max_freq - 1) * (n + 1) + max_count
        
        # Final answer is the maximum of:
        # 1. Total tasks
        # 2. Calculated intervals with idle slots
        return max(len(tasks), intervals)