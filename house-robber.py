# https://neetcode.io/problems/house-robber/solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        def dfs(self, i: int, nums: List[int]) -> int:
            if i > len(nums) - 1:
                return 0
            if memo[i]:
                return memo[i]
            memo[i] = max(nums[i] + dfs(self,i+2,nums), dfs(self,i+1,nums))
            return memo[i]
        
        return dfs(self,0,nums)
        