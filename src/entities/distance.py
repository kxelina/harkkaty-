#from entities.trie import Trie

class Distance:
    def length(self, a, b):
        length_a = len(a)
        length_b = len(b)
        return self.distance(length_a, length_b)

    def distance(self, a, b):
        # if a and b == 0:
        #     return 0
        # if b > 0:
        #     return b
        # return a+b
        if a == 0:
            return b
        if b == 0:
            return a

       
    
    def optimal_string_alignment_distance(self, s1, s2):
    # Create a table to store the results of subproblems
        dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        
        # Initialize the table
        for i in range(len(s1)+1):
            dp[i][0] = i
        for j in range(len(s2)+1):
            dp[0][j] = j
    
        # Populate the table using dynamic programming
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
        # Return the edit distance
        return dp[len(s1)][len(s2)]
