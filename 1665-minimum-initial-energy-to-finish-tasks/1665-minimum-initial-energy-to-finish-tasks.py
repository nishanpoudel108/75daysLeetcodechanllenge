class Solution(object):
    def minimumEffort(self, tasks):
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        ans = 0

        for actual, minimum in tasks:

            # Need extra energy to start this task
            if energy < minimum:
                ans += (minimum - energy)
                energy = minimum

            # Finish task
            energy -= actual

        return ans