class Knapsack:

    def __init__(self, values, weights, capacity):
        self.values = values
        self.weights = weights
        self.capacity = capacity


    def knapsack_top_down(self):
        # data structure for memoization
        memo = {}
        
        # i: ith item, rc: remaining capacity
        # dp(i, rc): function for subproblem
        def dp(i, rc):
            i_weight = self.weights[i]
            i_val = self.values[i]

            # base cases
            if i == -1 or rc <= 0:
                return 0
                
            if (i, rc) in memo:
                return memo[(i, rc)]

            # DFS section
            # recurrence relation
            if i_weight > rc:
                max_val = dp(i-1, rc)
            else:
                max_val = max(dp(i-1, rc), dp(i-1, rc-i_weight) + i_val)

            memo[(i, rc)] = max_val
            
            return max_val

        return dp(len(self.values)-1, self.capacity)


    def knapsack_bottom_up_v1(self):
        N = len(self.values)
        C = self.capacity

        # table
        dp = [[0 for rc in range(C+1)] for i in range(N)]

        # filling out the table
        for i in range(0, N):
            i_weight = self.weights[i]
            i_val = self.values[i]
            for rc in range(1, C+1):
                # edge case
                if i == 0:
                    if i_weight > rc:
                        dp[i][rc] = 0
                    else:
                        dp[i][rc] = i_val
                # recurrence relation
                if i_weight > rc:
                    dp[i][rc] = dp[i-1][rc]
                else:
                    dp[i][rc] = max(dp[i-1][rc], dp[i-1][rc-i_weight] + i_val)
        return dp[N-1][C]


    def knapsack_bottom_up_v2(self):
        N = len(self.values)
        C = self.capacity

        # prev_dp == dp[i-1]
        prev_dp = [0]*(C+1)
        # dp == dp[i]
        dp = [0]*(C+1)

        # filling out the table
        for i in range(0, N):
            i_weight = self.weights[i]
            i_val = self.values[i]
            for rc in range(1, C+1):
                # recurrence relation
                if i_weight > rc:
                    dp[rc] = prev_dp[rc]
                else:
                    dp[rc] = max(prev_dp[rc], prev_dp[rc-i_weight] + i_val)
            prev_dp, dp = dp, prev_dp
            # clear current row
            for i in range(len(dp)):
                dp[i] = 0

        return prev_dp[C]


    def knapsack_bottom_up_v3(self):
        N = len(self.values)
        C = self.capacity
        dp = [0]*(C+1)
        for i in range(0, N):
            # inner loop is looping backwards
            # there is no need to check for i_weight > rc
            # if i_wieght > rc, the loop won't run, and it would automatically have the prev_row value
            i_weight = self.weights[i]
            i_val = self.values[i]
            for rc in range(C, i_weight-1, -1):
                dp[rc] = max(dp[rc], dp[rc-i_weight] + i_val)
        return dp[C]
