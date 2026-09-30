class Solution:
    def twoSum(self, nums, target):
        exists = {}
        for index , value in enumerate(nums):
            complement = target - value
            if complement in exists:
                return [exists[complement], index]
            exists[value] = index
        return []

