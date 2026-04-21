# https://leetcode.com/problems/product-of-array-except-self/description/
# Intuition: To solve the problem of finding the product of an array except for the current index, 
# we can use a two-pass approach. In the first pass, we calculate the cumulative product from the 
# left side and store it in an answer array. 
# In the second pass, we calculate the cumulative product from the right side and multiply it with 
# the corresponding value in the answer array. 
# 

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        # O(n) solution
        length = len(nums)
        l = [0] * length
        l[0] = nums[0]
        r = [0] * length
        r[length-1] = nums[length-1]
        answer = [0] *length

        for i in range(1,length):
            l[i] = nums[i] * l[i-1]
        for j in range(length-1,0,-1):
            r[j-1] = r[j] * nums[j-1]
        answer[0] = r[1]
        answer[length-1] = l[length-2]
        for k in range(1,length-1):
                answer[k] = l[k-1] * r[k+1]

        return answer
        '''
        # nums [1,2,3,4]
        # l [1,2,6,24]
        # r [24,24,12,4]
        # answer [24,12,8,6]

        # for O(1)
        # answer [24,24,12,4]

        # O(1) space complexity solution

        length = len(nums)
        answer = [0] *length
        answer[length-1] = nums[length-1]

        # store prefix in answer array
        for j in range(length-1,0,-1):
            answer[j-1] = answer[j] * nums[j-1]
        # print(answer)
        # iterate through nums and store cumulative product only
        left = nums[0]
        answer[0] = answer[1]
        # left = left * answer[1]
        # answer[1] = left * answer[2]
        # answer[2] = left * answer[3]
        for i in range(2,length):
            answer[i-1] = left * answer[i]
            left *= nums[i-1]
        answer[length-1] = left
        return answer
    
class Solution2:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res