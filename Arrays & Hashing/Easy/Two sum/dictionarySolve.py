class Solution:
    def TwoSum(self, nums: list, target: int) -> list:
        my_dict = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in my_dict:
                return [my_dict[n], i]
            my_dict[num] = i