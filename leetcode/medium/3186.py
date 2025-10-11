class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        from collections import Counter
        
        # Count frequency of each damage value
        freq = Counter(power)
        
        # Get unique sorted damage values
        unique_damages = sorted(freq.keys())
        
        if not unique_damages:
            return 0
        
        n = len(unique_damages)
        if n == 1:
            return unique_damages[0] * freq[unique_damages[0]]
        
        # dp[i] = max damage we can get considering damages[0..i]
        dp = [0] * n
        
        # Base case: take all instances of first damage value
        dp[0] = unique_damages[0] * freq[unique_damages[0]]
        
        # For second element
        if unique_damages[1] - unique_damages[0] <= 2:
            # Can't take both, choose better one
            dp[1] = max(dp[0], unique_damages[1] * freq[unique_damages[1]])
        else:
            # Can take both
            dp[1] = dp[0] + unique_damages[1] * freq[unique_damages[1]]
        
        # Fill dp table
        for i in range(2, n):
            current_damage = unique_damages[i] * freq[unique_damages[i]]
            
            # Option 1: Don't take current damage
            dp[i] = dp[i - 1]
            
            # Option 2: Take current damage
            # Find the last index we can take with current
            j = i - 1
            while j >= 0 and unique_damages[i] - unique_damages[j] <= 2:
                j -= 1
            
            if j >= 0:
                dp[i] = max(dp[i], dp[j] + current_damage)
            else:
                dp[i] = max(dp[i], current_damage)
        
        return dp[n - 1]
        