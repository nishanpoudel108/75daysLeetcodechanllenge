from bisect import bisect_right

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):
        INF = float('inf')

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x[0] for x in rides]
            d = [x[1] for x in rides]
            n = len(rides)

            pref_min_d = [0] * n
            pref_min_d[0] = d[0]
            for i in range(1, n):
                pref_min_d[i] = min(pref_min_d[i - 1], d[i])

            suff_min_sd = [INF] * (n + 1)
            for i in range(n - 1, -1, -1):
                suff_min_sd[i] = min(suff_min_sd[i + 1], s[i] + d[i])

            return s, pref_min_d, suff_min_sd

        # Structures for water rides (used when land is taken first)
        w_starts, w_pref_d, w_suff_sd = build(
            waterStartTime, waterDuration
        )

        # Structures for land rides (used when water is taken first)
        l_starts, l_pref_d, l_suff_sd = build(
            landStartTime, landDuration
        )

        ans = INF

        # Land -> Water
        for ls, ld in zip(landStartTime, landDuration):
            land_end = ls + ld

            k = bisect_right(w_starts, land_end)

            best = INF
            if k > 0:
                best = min(best, land_end + w_pref_d[k - 1])
            best = min(best, w_suff_sd[k])

            ans = min(ans, best)

        # Water -> Land
        for ws, wd in zip(waterStartTime, waterDuration):
            water_end = ws + wd

            k = bisect_right(l_starts, water_end)

            best = INF
            if k > 0:
                best = min(best, water_end + l_pref_d[k - 1])
            best = min(best, l_suff_sd[k])

            ans = min(ans, best)

        return ans