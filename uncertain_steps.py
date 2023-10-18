# Python Program to find n-th stair using step size
# 1 or 2 or 3.
class CS:

	def findStepHelper(self, n, dp):
	
		# Base Case
		if (n == 0):
			return 1
		elif (n < 0):
			return 0
			
		# If subproblems are already calculated
		#then return it
		if (dp[n] != -1):
			return dp[n]

		# store the subproblems in the vector
		dp[n] = self.findStepHelper(n - 3, dp) + self.findStepHelper(n - 2, dp) + self.findStepHelper(n - 1, dp)
		
		return dp[n]

	# Returns count of ways to reach n-th stair
	# using 1 or 2 or 3 steps.
	def findStep(self, n):

		dp = [-1 for i in range(n + 1)]
		return self.findStepHelper(n, dp)

# Driver code
g = CS()
n = 4

print(g.findStep(n))

