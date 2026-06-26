class Solution:
    def twoSum(self, nums, target):
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    paired_value = i,j
                    pairs.append(paired_value)
        return pairs
    def print_result(self, nums_result, target_1):
        print(Solution.twoSum(self, nums_result, target_1))
    

 

            
x = Solution()

# nums = [1, 2, 3, 4, 5, 76, 7]
nums_1 = [3, 3, 3, 3, 3]

target = 6

# x.twoSum(nums, target)
x.print_result(nums_1, target)


