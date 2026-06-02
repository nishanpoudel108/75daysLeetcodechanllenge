class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(waterStartTime[j], land_finish)
                ans = min(ans, water_start + waterDuration[j])

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(landStartTime[i], water_finish)
                ans = min(ans, land_start + landDuration[i])

        return ans