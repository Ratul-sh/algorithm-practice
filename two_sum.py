class Solution_bruteForce:
    def twoSum(self, nums, target):
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    paired_value = i,j
                    pairs.append(paired_value)
        return pairs
    def print_result(self, nums_result, target_1):
        print(Solution_bruteForce.twoSum(self, nums_result, target_1))
    

class Solution_withDict:
    def twoSum(self, nums, target):
        storage = {}
        for index, value in enumerate(nums):
            complementory_value = target - value
            if complementory_value in storage:
                return [storage[complementory_value], index]
            else:
                storage[value] = index
        
    
    def show_result(self, nums_show, target_show):
        print(Solution_withDict.twoSum(self, nums_show, target_show))

            


            
x = Solution_bruteForce()
y = Solution_withDict()

# nums = [1, 2, 3, 4, 5, 76, 7]
nums_1 = [3, 3, 3, 3, 3]

target = 6

# x.twoSum(nums, target)
y.show_result(nums_1, target)


