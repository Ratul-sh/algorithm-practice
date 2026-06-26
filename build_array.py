class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
   
x = Solution()

y = x.buildArray([1,3,4,0,2])
print(y)

