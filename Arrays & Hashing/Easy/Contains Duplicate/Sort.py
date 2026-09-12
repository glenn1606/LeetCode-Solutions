
nums = [1, 1, 3, 4, 2, 6, 8, 6, 7, 9, 0]

class Solution:
    def hasDuplicates (self, nums: list[int]) -> bool:
        new_sorted_nums = sorted(nums)
        for i in range(len(new_sorted_nums)-1):
            if new_sorted_nums[i] == new_sorted_nums[i+1]:
                return True
        return False

s = Solution()
print(s.hasDuplicates(nums))

