from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            if n < 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1, length):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_wave = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            10,
                            10,
                            0
                        )
                        total_count += cnt
                        total_wave += wav

                    else:
                        if not started:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                10,
                                d,
                                1
                            )
                            total_count += cnt
                            total_wave += wav

                        else:
                            extra = 0

                            if length >= 2:
                                if ((prev1 > prev2 and prev1 > d) or
                                    (prev1 < prev2 and prev1 < d)):
                                    extra = 1

                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                prev1,
                                d,
                                length + 1
                            )

                            total_count += cnt
                            total_wave += wav + extra * cnt

                return (total_count, total_wave)

            return dp(0, True, False, 10, 10, 0)[1]

        return solve(num2) - solve(num1 - 1)