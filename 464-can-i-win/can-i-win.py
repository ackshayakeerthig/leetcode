class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        n = maxChoosableInteger

        if desiredTotal <= 0:
            return True

        total = n * (n + 1) // 2

        if total < desiredTotal:
            return False

        size = 1 << n

        # score[mask] = sum of all numbers used in mask
        score = [0] * size

        for mask in range(1, size):

            bit = mask & -mask

            bit_index = bit.bit_length() - 1

            number = bit_index + 1

            prev = mask ^ bit

            score[mask] = score[prev] + number

        # dp[mask] = can current player force a win?
        dp = [False] * size

        # Process states with more used numbers first
        for mask in range(size - 1, -1, -1):

            current_score = score[mask]

            for i in range(1, n + 1):

                bit = 1 << (i - 1)

                # Number i already used
                if mask & bit:
                    continue

                # Current player wins immediately
                if current_score + i >= desiredTotal:
                    dp[mask] = True
                    break

                new_mask = mask | bit

                # Opponent is in a losing state
                if not dp[new_mask]:
                    dp[mask] = True
                    break

        return dp[0]