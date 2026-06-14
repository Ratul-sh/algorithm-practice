class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
   
x = Solution()

y = x.buildArray([1,3,5,8,2])
print(y)

